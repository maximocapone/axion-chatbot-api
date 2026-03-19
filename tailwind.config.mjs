/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        copper: '#B87333',
        'brand-red': '#FF0347',
        'brand-red-hover': '#B8002E',
        'secondary-bg': '#F5F0E6',
        dark: '#1E1E1E',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
    },
  },
  plugins: [],
}
