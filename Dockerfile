# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Instalar dependências do sistema para o Selenium e o Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    libnss3 \
    libgconf-2-4 \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para o contêiner
COPY . .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script principal
CMD ["python", "robô/main.py"]
