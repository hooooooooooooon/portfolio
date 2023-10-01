import strawberry
from works import schema as works_schema


@strawberry.type
class Query(works_schema.Query):
    pass


@strawberry.type
class Mutation:
    pass


schema = strawberry.Schema(
    query=Query,
)