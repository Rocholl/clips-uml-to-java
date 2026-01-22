# 🎯 Template de Motia + Svelte

Este es un **template completo y listo para usar** que combina:

- **Backend**: Motia con Steps en Python
- **Frontend**: Svelte con Vite
- **Herramientas**: Configuración completa de desarrollo

## 🚀 Inicio Rápido

```bash
# 1. Instalar dependencias
make setup

# 2. Iniciar desarrollo
make dev-all

# 3. Abrir en el navegador
# Backend: http://localhost:8080
# Frontend: http://localhost:3000
```

## 📦 ¿Qué incluye este template?

### Backend (Motia)
- ✅ Step de ejemplo (`src/example.step.py`)
- ✅ Configuración de Python (pyproject.toml, .flake8)
- ✅ Estructura lista para añadir más Steps

### Frontend (Svelte)
- ✅ Componente principal con ejemplo de integración
- ✅ Configuración de Vite con proxy al backend
- ✅ Estilos modernos y responsivos

### Herramientas de Desarrollo
- ✅ **Makefile**: Comandos útiles para desarrollo
- ✅ **Prettier**: Formateo automático de código
- ✅ **Black**: Formateo automático de Python
- ✅ **Flake8**: Linting de Python
- ✅ **EditorConfig**: Consistencia en editores
- ✅ **VS Code**: Configuración recomendada

### Documentación
- ✅ README completo
- ✅ Guía de arquitectura
- ✅ Guía de contribución

## 🎨 Personalización

### 1. Crear un nuevo Step

Crea un archivo `src/mi-step.step.py`:

```python
from datetime import datetime

config = {
    'name': 'MiStep',
    'type': 'api',
    'path': '/mi-endpoint',
    'method': 'POST',
}

async def handler(req, context):
    logger = context.get('logger') if context else None
    body = req.get('body', {}) if isinstance(req, dict) else {}
    
    # Tu lógica aquí
    
    return {
        'status': 200,
        'body': {'mensaje': '¡Funciona!'}
    }
```

### 2. Modificar el Frontend

Edita `frontend/src/App.svelte` para personalizar la interfaz.

### 3. Añadir Dependencias

**Python**: Añade a `requirements.txt` o `pyproject.toml`

**JavaScript**: 
```bash
# Backend
npm install <paquete>

# Frontend
cd frontend && npm install <paquete>
```

## 📚 Recursos

- [Documentación de Motia](https://www.motia.dev/docs)
- [Documentación de Svelte](https://svelte.dev/docs)
- [Documentación de Vite](https://vitejs.dev/)

## 🔄 Mantenimiento

Este template se actualiza regularmente. Para actualizar:

```bash
git pull origin main
make install
```

## 📝 Notas

- El Step de ejemplo (`example.step.py`) puede eliminarse cuando crees tus propios Steps
- El componente `App.svelte` es solo un ejemplo - personalízalo completamente
- Todas las configuraciones están listas para producción

## 🆘 ¿Problemas?

1. Verifica que tienes Python 3.8+ y Node.js 18+
2. Asegúrate de tener Motia CLI instalado: `npm install -g @motia/cli`
3. Consulta la [documentación de Motia](https://www.motia.dev/docs)

---

**¡Listo para empezar!** 🎉
