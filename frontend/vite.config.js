import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  server: {
    port: 3000,
    host: '0.0.0.0', // Permite acceso desde fuera del contenedor
    proxy: {
      '/example': {
        // En Docker: usa el nombre del servicio 'backend' en el puerto 8080
        // En local: usa localhost:8080
        target: process.env.VITE_API_URL || 'http://localhost:8080',
        changeOrigin: true,
        secure: false,
        ws: true, // Para WebSocket si es necesario
      },
    },
  },
});
