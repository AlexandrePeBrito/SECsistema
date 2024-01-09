FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criar o diretório de trabalho no contêiner
WORKDIR /app

# Copiar arquivos necessários para o contêiner
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos para o contêiner
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

# Executar migrações, gerar a API e outras configurações iniciais
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py generate-api -f

# Comando padrão para iniciar a aplicação
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
