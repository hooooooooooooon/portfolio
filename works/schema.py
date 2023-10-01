import strawberry
import typing
from . import types
from . import queries


@strawberry.type
class Query:
    all_works: typing.List[types.WorkType] = strawberry.field(
        resolver=queries.get_all_works,
    )
    work: typing.Optional[types.WorkType] = strawberry.field(
        resolver=queries.get_work
    )