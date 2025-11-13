# gql-book-server

A GraphQL server with Strawberry and FastAPI, supporting HTTP multipart subscriptions:

https://www.apollographql.com/docs/graphos/routing/operations/subscriptions/multipart-protocol

👉 **Public URL**: https://gql-book-server.fly.dev/graphql

## Try it out!

Use the following query in GraphiQL to test a subscription:

```graphql
subscription {
  book {
    title
    author
  }
}
```

...or with curl:

```bash
curl -XPOST http://0.0.0.0:8080/graphql \
  -H 'content-type: application/json' \
  -H 'accept: multipart/mixed;subscriptionSpec="1.0", application/json' \
  -d '{"query":"subscription { book { id title author } }"}'
```
