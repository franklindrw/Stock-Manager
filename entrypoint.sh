#!/bin/bash

# Aborta o script se qualquer comando falhar
set -e

# 1. Aguardar o Postgres estar pronto para receber conexões
# Isso evita que o Alembic falhe porque o container do banco ainda está "acordando"
echo "--- Aguardando PostgreSQL ---"

# Usamos um loop simples com o pg_isready (que já vem no cliente postgres)
until uv run python -c "import psycopg2; psycopg2.connect('$DATABASE_URL')" 2>/dev/null; do
  echo "Postgres ainda está indisponível - aguardando..."
  sleep 2
done

echo "--- Postgres está UP! ---"

# 2. Validar e Aplicar Migrações
echo "--- Verificando e aplicando migrações do Alembic ---"
uv run alembic upgrade head

# 3. Iniciar a Aplicação
# Usando 'exec' para que a aplicação vire o processo principal (PID 1) do container
# Isso é vital para que o container receba sinais de parada (SIGTERM) corretamente
echo "--- Iniciando a API ---"
exec uv run python src/app/main.py