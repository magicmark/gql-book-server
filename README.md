# gql-book-server

A GraphQL server with Strawberry and FastAPI, supporting HTTP multipart subscriptions:

https://www.apollographql.com/docs/graphos/routing/operations/subscriptions/multipart-protocol

## Try it out!

👉 **Public URL**: https://gql-book-server.fly.dev/graphql

...or with curl:

```bash
curl -XPOST http://0.0.0.0:8080/graphql \
  -H 'content-type: application/json' \
  -H 'Accept: multipart/mixed;subscriptionSpec="1.0", application/json' \
  -d '{"query":"subscription { book(target: 3) { id title author } }"}'
```
