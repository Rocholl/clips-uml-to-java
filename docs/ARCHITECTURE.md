# Arquitectura del Proyecto

## Visión General

Este proyecto utiliza una arquitectura de **backend y frontend separados**:

- **Backend**: Motia con Steps en Python
- **Frontend**: Svelte con Vite

## Backend (Motia)

### Estructura

Los Steps de Motia se encuentran en `src/` y siguen el patrón:

```python
config = {
    'name': 'StepName',
    'type': 'api',  # o 'event', 'workflow', etc.
    'path': '/endpoint',
    'method': 'POST',
}

async def handler(req, context):
    # Lógica del handler
    return {'status': 200, 'body': {...}}
```

### Tipos de Steps

- **API Steps**: Endpoints REST que responden a requests HTTP
- **Event Steps**: Procesan eventos de forma asíncrona
- **Workflow Steps**: Orquestan múltiples pasos

### Flujo de Datos

```
Cliente HTTP → Motia Runtime → Step Handler → Response
```

## Frontend (Svelte)

### Estructura

```
frontend/
├── src/
│   ├── App.svelte      # Componente principal
│   ├── main.js        # Punto de entrada
│   └── app.css        # Estilos globales
├── index.html         # HTML base
└── vite.config.js     # Configuración de Vite
```

### Comunicación con Backend

El frontend se comunica con el backend mediante:

1. **Proxy de Vite**: Configurado en `vite.config.js` para desarrollo
2. **Fetch API**: Para hacer requests HTTP
3. **Endpoints REST**: Los Steps de Motia exponen endpoints REST

### Flujo de Datos

```
Usuario → Svelte Component → Fetch API → Motia Backend → Response → UI Update
```

## Configuración de Desarrollo

### Variables de Entorno

- `.env.example`: Template de variables de entorno
- `.env`: Variables reales (no versionado)

### Scripts

- `npm run dev`: Inicia backend Motia
- `npm run dev:frontend`: Inicia frontend Svelte
- `npm run dev:all`: Inicia ambos simultáneamente

## Despliegue

### Backend

Motia maneja el despliegue automáticamente:

```bash
npm run build
npm run start
```

### Frontend

Construir para producción:

```bash
cd frontend
npm run build
```

Los archivos estáticos se generan en `frontend/dist/`.

## Escalabilidad

- **Backend**: Cada Step escala independientemente
- **Frontend**: Puede servirse desde CDN o servidor estático
- **Comunicación**: HTTP/REST permite separación completa

## Seguridad

- Validación de inputs en el backend
- CORS configurado en Vite para desarrollo
- Variables sensibles en `.env` (no versionado)
