# Motia + Svelte Template

Una plantilla completa y lista para usar con **Motia (Python)** como backend y **Svelte** como frontend.

## 🚀 Características

- ✅ **Backend con Motia**: Steps en Python listos para usar
- ✅ **Frontend con Svelte**: Interfaz moderna y reactiva
- ✅ **Configuración completa**: Linting, formateo, y herramientas de desarrollo
- ✅ **Multi-lenguaje**: Backend en Python, frontend en JavaScript
- ✅ **Escalable**: Arquitectura preparada para crecer
- ✅ **Docker**: Configuración completa para desarrollo y producción

## 📁 Estructura del Proyecto

```
clips_modelos/
├── src/                         # Steps de Motia (backend)
│   └── example.step.py          # Step de ejemplo
├── frontend/                    # Aplicación Svelte
│   ├── src/
│   │   ├── App.svelte          # Componente principal
│   │   ├── main.js             # Punto de entrada
│   │   └── app.css             # Estilos globales
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
├── docs/                        # Documentación adicional
│   └── ARCHITECTURE.md         # Arquitectura del proyecto
├── .vscode/                     # Configuración de VS Code
│   ├── settings.json
│   └── extensions.json
├── package.json                 # Dependencias y scripts de Node.js
├── requirements.txt             # Dependencias de Python (opcional)
├── pyproject.toml              # Configuración de Python
├── Makefile                     # Comandos útiles (make)
├── .editorconfig               # Configuración del editor
├── .prettierrc                 # Configuración de Prettier
├── .flake8                      # Configuración de Flake8
├── .gitignore                  # Archivos ignorados por Git
├── CONTRIBUTING.md             # Guía de contribución
├── DOCKER.md                   # Guía de Docker
├── Dockerfile                  # Dockerfile para backend (desarrollo)
├── Dockerfile.prod            # Dockerfile para backend (producción)
├── docker-compose.yml          # Docker Compose para desarrollo
├── docker-compose.prod.yml     # Docker Compose para producción
└── README.md                   # Este archivo
```

## 🛠️ Instalación Rápida

### Opción 1: Usando Make (Recomendado)

```bash
# Configurar todo el proyecto
make setup

# O manualmente:
make install
cp .env.example .env
```

### Opción 2: Manual

1. **Asegúrate de tener Python 3.8+ y Node.js 18+ instalados:**
   ```bash
   python --version  # o python3 --version
   node --version
   ```

2. **Instala todas las dependencias:**
   ```bash
   npm run install:all
   ```

3. **Configura variables de entorno:**
   ```bash
   cp .env.example .env
   ```

4. **Instala Motia CLI globalmente:**
   ```bash
   npm install -g @motia/cli
   ```

## 🎯 Uso

### Opción 1: Desarrollo Local (Sin Docker)

**Iniciar backend y frontend simultáneamente (Recomendado)**
```bash
make dev-all
# o
npm run dev:all
```

**Iniciar por separado**

Terminal 1 - Backend:
```bash
make dev
# o
npm run dev
```

Terminal 2 - Frontend:
```bash
make dev-frontend
# o
npm run dev:frontend
```

### Opción 2: Desarrollo con Docker (Recomendado)

```bash
# Construir e iniciar contenedores
make docker-up
# o
docker-compose up -d
```

Esto iniciará:
- **Backend**: http://localhost:8080
- **Frontend**: http://localhost:3000

Ver logs:
```bash
make docker-logs
```

Detener:
```bash
make docker-down
```

Consulta [DOCKER.md](DOCKER.md) para más información sobre Docker.

### Comandos Disponibles

Usando **Make**:
```bash
make help          # Ver todos los comandos disponibles
make setup         # Configurar proyecto completo
make install       # Instalar dependencias
make dev-all       # Iniciar backend y frontend
make build         # Construir para producción
make clean         # Limpiar archivos generados
make format        # Formatear código
make lint          # Verificar estilo de código
make lint-fix      # Corregir problemas de estilo
```

Usando **npm**:
```bash
npm run dev              # Backend solamente
npm run dev:frontend     # Frontend solamente
npm run dev:all          # Backend y frontend
npm run build            # Construir backend
npm run build:frontend   # Construir frontend
npm run build:all        # Construir todo
npm run format           # Formatear código
npm run lint:python      # Lint Python
npm run lint:python:fix  # Corregir Python
```

## 📝 Crear tu Primer Step

1. **Crea un nuevo archivo** en `src/` con extensión `.step.py`:

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
    
    if logger:
        logger.info('Mi Step ejecutado')
    
    return {
        'status': 200,
        'body': {'mensaje': '¡Hola desde Motia!'}
    }
```

2. **Motia detectará automáticamente** el nuevo Step
3. **Accede al endpoint** desde tu frontend o con curl

## 📡 API Endpoint de Ejemplo

El template incluye un Step de ejemplo:

- **URL**: `GET /example?name=TuNombre`
- **Response**: `{"message": "Hola, TuNombre!", "timestamp": "...", "example": true}`

Prueba con:
```bash
curl http://localhost:8080/example?name=Mundo
```

## 🎨 Personalizar el Frontend

1. Edita `frontend/src/App.svelte` para modificar la interfaz
2. Añade nuevos componentes en `frontend/src/components/`
3. Modifica los estilos en `frontend/src/app.css`

## 📚 Documentación Adicional

- [Arquitectura del Proyecto](docs/ARCHITECTURE.md) - Detalles sobre la estructura y diseño
- [Guía de Contribución](CONTRIBUTING.md) - Cómo contribuir al proyecto
- [Guía de Docker](DOCKER.md) - Uso de Docker para desarrollo y producción
- [Documentación de Motia](https://www.motia.dev/docs) - Documentación oficial

## 🛠️ Herramientas de Desarrollo

El proyecto incluye configuración para:

- **EditorConfig**: Consistencia en diferentes editores
- **Prettier**: Formateo automático de código JavaScript/Svelte
- **Black**: Formateo automático de código Python
- **Flake8**: Linting de Python
- **VS Code**: Configuración recomendada y extensiones

## 🔧 Tipos de Steps en Motia

- **API Steps**: Endpoints REST (`type: 'api'`)
- **Event Steps**: Procesamiento asíncrono (`type: 'event'`)
- **Workflow Steps**: Orquestación compleja (`type: 'workflow'`)

Consulta la [documentación de Motia](https://www.motia.dev/docs) para más detalles.

## 📝 Scripts Útiles

Ver todos los comandos disponibles:
```bash
make help
```

Formatear todo el código:
```bash
make format
```

Verificar estilo sin modificar:
```bash
make lint
```

Limpiar archivos generados:
```bash
make clean
```

## 🚀 Próximos Pasos

1. Crea tus propios Steps en `src/`
2. Personaliza el frontend en `frontend/src/`
3. Añade más funcionalidades según tus necesidades
4. Consulta la documentación de Motia para features avanzadas

## 📄 Licencia

MIT

---

**¿Necesitas ayuda?** Consulta la [documentación de Motia](https://www.motia.dev/docs) o abre un issue.
