from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import logging

# Carga variables de entorno desde .env (en producción Railway las inyecta directamente)
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Validación temprana de la API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY no está configurada. Añádela como variable de entorno.")

# Orígenes permitidos (configura ALLOWED_ORIGIN en Railway con tu dominio)
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN", "*")

# Referencia global a la cadena RAG
rag_chain = None


app = FastAPI(title="AXION Chatbot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN] if ALLOWED_ORIGIN != "*" else ["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


# --- Modelos de datos ---
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str


# --- Construcción del RAG ---
def build_rag_chain():
    """Carga los documentos de /docs y construye la cadena RAG."""
    docs_path = os.path.join(os.path.dirname(__file__), "docs")

    # Carga archivos .txt
    txt_loader = DirectoryLoader(docs_path, glob="*.txt", loader_cls=TextLoader, silent_errors=True)
    txt_docs = txt_loader.load()

    # Carga archivos .pdf
    pdf_loader = PyPDFDirectoryLoader(docs_path, silent_errors=True)
    pdf_docs = pdf_loader.load()

    documents = txt_docs + pdf_docs
    if not documents:
        raise RuntimeError(f"No se encontraron documentos .txt ni .pdf en {docs_path}")
    logger.info(f"{len(documents)} documento(s) cargado(s) ({len(txt_docs)} txt, {len(pdf_docs)} pdf).")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(chunks, embeddings)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=OPENAI_API_KEY)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    )
    return chain


def get_rag_chain():
    global rag_chain
    if rag_chain is None:
        logger.info("Inicializando RAG bajo demanda...")
        rag_chain = build_rag_chain()
        logger.info("RAG listo.")
    return rag_chain



# --- Endpoints ---
@app.get("/")
def health_check():
    return {"status": "ok", "rag_initialized": rag_chain is not None}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    
    try:
        chain = get_rag_chain()
        result = chain.invoke({"query": request.message})
        return ChatResponse(reply=result["result"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
