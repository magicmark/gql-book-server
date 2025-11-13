FROM python:3.13-bookworm AS builder

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
COPY gql_book_server ./gql_book_server
RUN pip install uv
RUN uv sync --frozen

FROM python:3.13-slim-bookworm

ENV PYTHONPATH=/app

WORKDIR /app
COPY --from=builder /app/.venv .venv/
COPY gql_book_server ./gql_book_server
CMD ["/app/.venv/bin/python3", "-m", "uvicorn", "gql_book_server.fastapi_server:app", "--host", "0.0.0.0", "--port", "8080"]

