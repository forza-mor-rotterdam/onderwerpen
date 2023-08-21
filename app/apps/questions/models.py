from django.contrib.gis.db import models
from utils.fields import DictJSONField
from utils.models import BaseModel


class Question(BaseModel):
    class FieldTypeOptions(models.TextChoices):
        TEXT = "text", "Text"
        LONG_TEXT = "long-text", "Long text"
        INTEGER = "integer", "Integer"
        NUMBER = "number", "Number"
        BOOL = "bool", "Bool"

    sort = models.IntegerField(default=0)
    key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    public_name = models.CharField(max_length=255)
    field_type = models.CharField(
        max_length=125,
        choices=FieldTypeOptions.choices,
        default=FieldTypeOptions.TEXT,
    )
    description = models.TextField(blank=True, null=True)
    required = models.BooleanField(default=True)
    meta = DictJSONField(default=dict)
    category = models.ForeignKey(
        to="categories.Category",
        on_delete=models.CASCADE,
        related_name="questions",
    )

    def __str__(self) -> str:
        return f"{self.name}, pk: {self.pk}"

    class Meta:
        abstract = False
