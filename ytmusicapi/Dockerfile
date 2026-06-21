# ytmusic-api/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala Flask e requests
RUN pip install --no-cache-dir flask requests

# Copia o projeto inteiro para dentro do container
COPY . /app/ytmusicapi_src

# setuptools-scm precisa do git para detectar a versão;
# como o .git não está no container, simulamos a versão via env var
ENV SETUPTOOLS_SCM_PRETEND_VERSION_FOR_YTMUSICAPI=1.0.0

# Instala o pacote ytmusicapi a partir do fonte local
RUN pip install --no-cache-dir /app/ytmusicapi_src

# Copia o app Flask para o diretório de trabalho
COPY ytmusicapi/app.py /app/app.py

EXPOSE 3001

CMD ["python", "app.py"]