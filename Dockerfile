# Dockerfile para Backend Motia (Python)
FROM python:3.11-slim

# Instalar Node.js y herramientas (necesario para Motia CLI)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js 18
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de configuración
COPY package.json package-lock.json* ./
COPY requirements.txt ./
COPY pyproject.toml ./

# Instalar dependencias de Node.js
RUN npm install

# Instalar dependencias de Python (si hay alguna)
RUN pip install --no-cache-dir -r requirements.txt || true

# Copiar código fuente
COPY src/ ./src/

# Exponer puerto
EXPOSE 8080

# Nota: Motia CLI debe instalarse manualmente o desde su fuente oficial
# Por ahora, ejecutamos un servidor Python simple con CORS como placeholder
# Reemplaza esto con el comando correcto de Motia cuando esté disponible
CMD ["python", "src/server.py"]
