# AXION Chatbot API

API REST con FastAPI + LangChain RAG lista para deployar en Railway.

## Estructura

```
chatbot-api/
  main.py           → Servidor FastAPI con endpoint /chat
  requirements.txt  → Dependencias Python
  railway.toml      → Configuración de Railway
  runtime.txt       → Versión de Python (3.11)
  Procfile          → Comando de arranque alternativo
  .env.example      → Plantilla de variables de entorno
  docs/             → Carpeta con tus archivos .txt de conocimiento
```

## Variables de entorno requeridas

| Variable         | Descripción                                      |
|------------------|--------------------------------------------------|
| `OPENAI_API_KEY` | Tu clave de OpenAI (obligatoria)                 |
| `ALLOWED_ORIGIN` | Dominio de tu web Astro (ej: https://tudominio.com) |

## Endpoints

| Método | Ruta    | Descripción                    |
|--------|---------|--------------------------------|
| GET    | `/`     | Health check                   |
| POST   | `/chat` | Envía un mensaje al chatbot    |

### Ejemplo de request POST /chat

```json
{
  "message": "¿Qué servicios ofrece AXION?"
}
```

### Ejemplo de response

```json
{
  "reply": "AXION ofrece desarrollo de chatbots con IA, automatización con agentes..."
}
```

## Personalizar el conocimiento del chatbot

Edita o agrega archivos `.txt` en la carpeta `docs/`. El chatbot los leerá automáticamente al iniciar.

## Deploy en Railway

1. Sube esta carpeta a un repositorio de GitHub
2. En [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Añade las variables de entorno: `OPENAI_API_KEY` y `ALLOWED_ORIGIN`
4. Railway detecta `railway.toml` y despliega automáticamente

## Prueba local

```bash
pip install -r requirements.txt
cp .env.example .env   # edita .env con tu API key real
uvicorn main:app --reload
```

Documentación interactiva disponible en: `http://localhost:8000/docs`
