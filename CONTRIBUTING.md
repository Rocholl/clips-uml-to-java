# Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto!

## Configuración del Entorno de Desarrollo

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd clips_modelos
   ```

2. **Configurar el proyecto**
   ```bash
   make setup
   # o manualmente:
   npm run install:all
   cp .env.example .env
   ```

3. **Iniciar el desarrollo**
   ```bash
   make dev-all
   # o manualmente:
   npm run dev:all
   ```

## Estándares de Código

### Python
- Usa **Black** para formateo automático
- Sigue **PEP 8** con las excepciones en `.flake8`
- Línea máxima: 100 caracteres
- Usa type hints cuando sea posible

```bash
# Formatear código Python
make lint-fix
# o
npm run lint:python:fix
```

### JavaScript/Svelte
- Usa **Prettier** para formateo automático
- Sigue las reglas en `.prettierrc`
- Usa ES6+ cuando sea posible

```bash
# Formatear código frontend
npm run format
```

## Estructura del Proyecto

```
clips_modelos/
├── src/                    # Steps de Motia (backend)
│   └── *.step.py          # Steps en Python
├── frontend/               # Aplicación Svelte
│   ├── src/
│   │   ├── App.svelte     # Componente principal
│   │   └── *.svelte       # Otros componentes
│   └── ...
├── .editorconfig          # Configuración del editor
├── .prettierrc            # Configuración de Prettier
├── pyproject.toml         # Configuración de Python
└── Makefile               # Comandos útiles
```

## Proceso de Desarrollo

1. **Crear una rama**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

2. **Hacer cambios**
   - Escribe código limpio y bien documentado
   - Añade comentarios cuando sea necesario
   - Sigue los estándares de código

3. **Verificar el código**
   ```bash
   make lint
   make format
   ```

4. **Probar los cambios**
   ```bash
   make dev-all
   # Verifica que todo funcione correctamente
   ```

5. **Commit y Push**
   ```bash
   git add .
   git commit -m "feat: descripción de los cambios"
   git push origin feature/nueva-funcionalidad
   ```

## Convenciones de Commits

Usa [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, punto y coma faltante, etc.
- `refactor:` Refactorización de código
- `test:` Añadir o modificar tests
- `chore:` Cambios en build, dependencias, etc.

Ejemplo:
```
feat: añadir procesamiento de texto en mayúsculas
fix: corregir conteo de palabras con caracteres especiales
docs: actualizar README con instrucciones de instalación
```

## Añadir Nuevos Steps

Para añadir un nuevo Step de Motia:

1. Crea un archivo `nombre-del-step.step.py` en `src/`
2. Define `config` y `handler` según la documentación de Motia
3. Motia lo detectará automáticamente

Ejemplo:
```python
config = {
    'name': 'MiNuevoStep',
    'type': 'api',
    'path': '/mi-endpoint',
    'method': 'POST',
}

async def handler(req, context):
    # Tu lógica aquí
    return {'status': 200, 'body': {'mensaje': 'Hola'}}
```

## Preguntas

Si tienes preguntas, abre un issue en el repositorio.

¡Gracias por contribuir! 🎉
