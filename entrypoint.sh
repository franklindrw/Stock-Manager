#!/bin/bash

# Aborta o script se qualquer comando falhar
set -e


# Verifica se o banco de dados está acessível usando psycopg
echo "--- Aguardando PostgreSQL $POSTGRES_DB ---"

until uv run python -c "import psycopg; psycopg.connect('$DATABASE_URL')" 2>/dev/null; do
  echo "Postgres ainda está indisponível - aguardando..."
  sleep 2
done

echo "--- Postgres está UP! ---"

# Valida e Aplicar Migrações
echo "--- Verificando e aplicando migrações do Alembic ---"
uv run alembic upgrade head

# Executa o CMD da imagem
exec "$@"
