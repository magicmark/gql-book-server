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


def main():
    print("Starting FastAPI server with multipart subscription support...")
    print("GraphQL endpoint: http://0.0.0.0:8000/graphql")
    print("GraphQL IDE: http://0.0.0.0:8000/graphql (browser)")
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
