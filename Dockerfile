FROM python:3.11-slim

WORKDIR /app

# Instalar compiladores + dependencias nativas (bcrypt y pyodbc) y utilidades para añadir repositorios
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg2 \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    build-essential \
    unixodbc \
    unixodbc-dev \
    freetds-dev \
    && rm -rf /var/lib/apt/lists/*

# Importar clave pública de Microsoft y agregar repositorio para msodbcsql18 (driver SQL Server)
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/24.04/prod noble main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]
