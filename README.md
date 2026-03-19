# AXION Web AI - Premium Landing Page

A fully bilingual (EN/ES), conversion-focused landing page built with Astro and Tailwind CSS.

## 🚀 Features

- ✅ **Bilingual Support**: English and Spanish with automatic detection and manual selector
- ✅ **Premium Design**: Copper (#B87333) and Red (#FF0347) brand colors
- ✅ **SEO Optimized**: Meta tags and semantic HTML
- ✅ **Responsive**: Mobile-first design
- ✅ **Animations**: Micro-animations and scroll effects
- ✅ **Performance**: Fast loading and optimized assets
- ✅ **Conversion-Focused**: Strategic CTAs and user flow

## 📁 Project Structure

```
ai-web-development/
├── src/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Hero.astro
│   │   ├── TrustSection.astro
│   │   ├── Services.astro
│   │   ├── Portfolio.astro
│   │   ├── Process.astro
│   │   ├── ValueSection.astro
│   │   ├── MidCTA.astro
│   │   ├── Contact.astro
│   │   └── Footer.astro
│   ├── i18n/
│   │   ├── ui.ts (translations)
│   │   └── utils.ts
│   ├── layouts/
│   │   └── BaseLayout.astro
│   └── pages/
│       ├── index.astro (redirects to /en)
│       ├── en/index.astro
│       └── es/index.astro
├── public/
│   ├── logo/
│   │   └── logo.png (place your logo here)
│   ├── hero/
│   │   ├── hero-bg.jpg
│   │   └── hero-image.jpg
│   └── portfolio/
│       ├── dashboard.jpg
│       ├── corporate.jpg
│       ├── portfolio.jpg
│       ├── saas.jpg
│       ├── mobile.jpg
│       └── ecommerce.jpg
└── package.json
```

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
npm install
```

### 2. Add Your Images

Place your images in the `public` folder:

- **Logo**: `public/logo/logo.png`
- **Hero Background**: `public/hero/hero-bg.jpg`
- **Hero Image**: `public/hero/hero-image.jpg`
- **Portfolio**: 6 project images in `public/portfolio/`

### 3. Run Development Server

```bash
npm run dev
```

Visit `http://localhost:4321`

### 4. Build for Production

```bash
npm run build
npm run preview
```

## 🌐 Internationalization

### Language Detection

The site automatically detects the user's browser language and redirects to the appropriate version:
- English: `/en`
- Spanish: `/es`

### Language Persistence

User's language preference is saved in `localStorage` and persists across sessions.

### Adding/Editing Translations

Edit [src/i18n/ui.ts](src/i18n/ui.ts) to modify translations.

## 🎨 Design System

### Colors

- **Background**: `#FFFFFF` (white)
- **Primary Text**: `#1E1E1E` (dark)
- **Brand Copper**: `#B87333`
- **Primary CTA**: `#FF0347` (red)
- **CTA Hover**: `#B8002E`
- **Secondary Background**: `#F5F0E6`

### Typography

- **Headings**: Playfair Display (serif)
- **Body**: Inter (sans-serif)

### Tailwind Classes

The design system is configured in [tailwind.config.mjs](tailwind.config.mjs):

```js
colors: {
  copper: '#B87333',
  'brand-red': '#FF0347',
  'brand-red-hover': '#B8002E',
  'secondary-bg': '#F5F0E6',
  dark: '#1E1E1E',
}
```

## 📄 Sections

1. **Header**: Sticky navigation with language selector
2. **Hero**: Large heading, subheadline, dual CTAs, background image
3. **Trust**: Social proof with client logos
4. **Services**: 4 service cards with icons and hover effects
5. **Portfolio**: 6 project showcases with zoom/overlay effects
6. **Process**: 4-step animated timeline
7. **Value Proposition**: Benefits with checkmarks
8. **Mid-CTA**: High-contrast red section
9. **Contact Form**: Full form with validation
10. **Footer**: Links, contact, language selector

## 🔧 Customization

### Changing Content

All text content is in [src/i18n/ui.ts](src/i18n/ui.ts). Edit the `ui` object to change any text on the site.

### Modifying Components

Each section is a separate Astro component in `src/components/`. Edit them individually to customize layout or behavior.

### Styling

The project uses Tailwind CSS utility classes. Modify component files to change styles, or extend the Tailwind config for custom utilities.

## 📧 Contact Form

The contact form currently uses a client-side simulation. To connect it to a real backend:

1. Replace the form submission handler in [src/components/Contact.astro](src/components/Contact.astro)
2. Add your API endpoint or email service (e.g., FormSpree, EmailJS, Netlify Forms)

## 🚀 Deployment

### Netlify / Vercel

1. Connect your repository
2. Build command: `npm run build`
3. Publish directory: `dist`

### Environment Variables

No environment variables required for basic deployment.

## 📝 License

This project is built for AXION Web AI.

---

**Built with ❤️ using Astro + Tailwind CSS**
