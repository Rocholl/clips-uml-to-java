.PHONY: help install dev build clean format lint test

help: ## Mostrar esta ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instalar todas las dependencias
	@echo "📦 Instalando dependencias del backend..."
	npm install
	@echo "📦 Instalando dependencias del frontend..."
	cd frontend && npm install
	@echo "✅ Dependencias instaladas"

dev: ## Iniciar servidor de desarrollo (backend)
	@echo "🚀 Iniciando backend Motia..."
	npm run dev

dev-frontend: ## Iniciar servidor de desarrollo (frontend)
	@echo "🚀 Iniciando frontend Svelte..."
	cd frontend && npm run dev

dev-all: ## Iniciar backend y frontend simultáneamente
	@echo "🚀 Iniciando backend y frontend..."
	npm run dev:all

build: ## Construir proyecto para producción
	@echo "🔨 Construyendo proyecto..."
	npm run build:all

clean: ## Limpiar archivos generados
	@echo "🧹 Limpiando archivos..."
	npm run clean
	@echo "✅ Limpieza completada"

format: ## Formatear código
	@echo "✨ Formateando código..."
	npm run format
	@echo "✅ Formateo completado"

lint: ## Verificar estilo de código
	@echo "🔍 Verificando estilo de código..."
	npm run lint:python
	npm run format:check
	@echo "✅ Verificación completada"

lint-fix: ## Corregir problemas de estilo
	@echo "🔧 Corrigiendo estilo de código..."
	npm run lint:python:fix
	npm run format
	@echo "✅ Corrección completada"

test: ## Ejecutar tests
	@echo "🧪 Ejecutando tests..."
	npm run test

setup: install ## Configurar proyecto completo
	@echo "📝 Copiando archivo .env.example a .env..."
	@if [ ! -f .env ]; then cp .env.example .env && echo "✅ Archivo .env creado"; fi
	@echo "✅ Proyecto configurado"

docker-build: ## Construir imágenes Docker
	@echo "🐳 Construyendo imágenes Docker..."
	docker-compose build
	@echo "✅ Imágenes construidas"

docker-up: ## Iniciar contenedores Docker (desarrollo)
	@echo "🐳 Iniciando contenedores Docker..."
	docker-compose up -d
	@echo "✅ Contenedores iniciados"
	@echo "📡 Backend: http://localhost:8080"
	@echo "🌐 Frontend: http://localhost:3000"

docker-down: ## Detener contenedores Docker
	@echo "🐳 Deteniendo contenedores Docker..."
	docker-compose down
	@echo "✅ Contenedores detenidos"

docker-logs: ## Ver logs de contenedores
	docker-compose logs -f

docker-restart: docker-down docker-up ## Reiniciar contenedores Docker

docker-prod-build: ## Construir imágenes para producción
	@echo "🐳 Construyendo imágenes de producción..."
	docker-compose -f docker-compose.prod.yml build
	@echo "✅ Imágenes de producción construidas"

docker-prod-up: ## Iniciar contenedores en producción
	@echo "🐳 Iniciando contenedores de producción..."
	docker-compose -f docker-compose.prod.yml up -d
	@echo "✅ Contenedores de producción iniciados"
	@echo "📡 Backend: http://localhost:8080"
	@echo "🌐 Frontend: http://localhost:80"

docker-prod-down: ## Detener contenedores de producción
	@echo "🐳 Deteniendo contenedores de producción..."
	docker-compose -f docker-compose.prod.yml down
	@echo "✅ Contenedores de producción detenidos"

docker-clean: ## Limpiar contenedores, imágenes y volúmenes
	@echo "🧹 Limpiando Docker..."
	docker-compose down -v --rmi all
	@echo "✅ Limpieza completada"
