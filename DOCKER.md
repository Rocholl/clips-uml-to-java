# 🐳 Guía de Docker

Esta guía explica cómo usar Docker con este proyecto.

## 📋 Requisitos

- Docker 20.10+
- Docker Compose 2.0+

Verificar instalación:
```bash
docker --version
docker-compose --version
```

## 🚀 Desarrollo con Docker

### Iniciar el proyecto

```bash
# Construir e iniciar contenedores
make docker-up
# o manualmente:
docker-compose up -d
```

Esto iniciará:
- **Backend**: http://localhost:8080
- **Frontend**: http://localhost:3000

### Ver logs

```bash
make docker-logs
# o
docker-compose logs -f
```

### Detener contenedores

```bash
make docker-down
# o
docker-compose down
```

### Reiniciar

```bash
make docker-restart
```

## 🏗️ Construcción Manual

### Backend

```bash
# Desarrollo
docker build -t motia-backend .

# Producción
docker build -f Dockerfile.prod -t motia-backend-prod .
```

### Frontend

```bash
# Desarrollo
docker build -f frontend/Dockerfile.dev -t motia-frontend-dev ./frontend

# Producción
docker build -f frontend/Dockerfile -t motia-frontend-prod ./frontend
```

## 🚢 Producción

### Construir y desplegar

```bash
# Construir imágenes de producción
make docker-prod-build
# o
docker-compose -f docker-compose.prod.yml build

# Iniciar en producción
make docker-prod-up
# o
docker-compose -f docker-compose.prod.yml up -d
```

### Variables de Entorno

Crea un archivo `.env` para producción:

```env
MOTIA_PORT=8080
MOTIA_ENV=production
NODE_ENV=production
```

## 🔧 Comandos Útiles

### Ver contenedores en ejecución

```bash
docker-compose ps
```

### Ejecutar comandos en contenedores

```bash
# Backend
docker-compose exec backend npm run build

# Frontend
docker-compose exec frontend npm run build
```

### Acceder al shell del contenedor

```bash
# Backend
docker-compose exec backend /bin/bash

# Frontend
docker-compose exec frontend /bin/sh
```

### Reconstruir sin caché

```bash
docker-compose build --no-cache
```

## 🧹 Limpieza

### Limpiar todo (contenedores, imágenes, volúmenes)

```bash
make docker-clean
# o
docker-compose down -v --rmi all
```

### Limpiar solo contenedores detenidos

```bash
docker-compose down
```

### Limpiar imágenes no utilizadas

```bash
docker image prune -a
```

## 📝 Estructura de Dockerfiles

### Backend

- **Dockerfile**: Desarrollo con hot-reload
- **Dockerfile.prod**: Producción optimizada con multi-stage build

### Frontend

- **Dockerfile.dev**: Desarrollo con Vite dev server
- **Dockerfile**: Producción con Nginx

## 🔍 Troubleshooting

### Puerto ya en uso

Si el puerto 8080 o 3000 está ocupado, modifica los puertos en `docker-compose.yml`:

```yaml
ports:
  - "8081:8080"  # Cambiar puerto host
```

### Permisos de archivos

Si hay problemas con permisos:

```bash
sudo chown -R $USER:$USER .
```

### Reconstruir desde cero

```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Ver logs de un servicio específico

```bash
docker-compose logs backend
docker-compose logs frontend
```

## 🌐 Redes

Los contenedores están en la misma red Docker (`motia-network`), por lo que pueden comunicarse usando los nombres de servicio:

- Backend: `http://backend:8080`
- Frontend: `http://frontend:3000`

## 📊 Health Checks

El backend incluye un health check que verifica que el servicio esté respondiendo:

```bash
# Verificar estado
docker-compose ps
```

## 🔐 Seguridad

Para producción, considera:

1. Usar secrets de Docker en lugar de variables de entorno en texto plano
2. Configurar HTTPS con un reverse proxy (Traefik, Nginx)
3. Limitar recursos con `deploy.resources` en docker-compose
4. Usar imágenes base más pequeñas (alpine)

## 📚 Recursos

- [Documentación de Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/)
