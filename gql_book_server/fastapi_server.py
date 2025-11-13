from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from gql_book_server.server import schema
import uvicorn

app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {
        "message": "GraphQL server with multipart subscription support",
        "graphql": "/graphql"
    }
