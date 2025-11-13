import typing
import random
import strawberry
from gql_book_server.books import Book, books
from typing import AsyncGenerator
import asyncio


@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return random.choice(books)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def book(self, target: int = 10) -> AsyncGenerator[Book, None]:
        for i in range(target):
            yield random.choice(books)
            await asyncio.sleep(0.5)


schema = strawberry.Schema(query=Query, subscription=Subscription)
