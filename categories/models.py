from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Pro or Edu Category Definition"""

    class CategoryKindChoices(models.TextChoices):
        PROFESSIONAL = "pro", "Pro"
        EDUCATIONAL = "edu", "Edu"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
