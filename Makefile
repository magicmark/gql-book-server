start-dev:
	uv run uvicorn gql_book_server.fastapi_server:app --host 0.0.0.0 --port 8080
