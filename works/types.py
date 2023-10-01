import strawberry
from strawberry import auto
from . import models
from users.types import UserType


@strawberry.django.type(models.Work)
class WorkType:
    id: auto
    main_title: auto
    owner: "UserType"