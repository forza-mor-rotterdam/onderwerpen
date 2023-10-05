from django.contrib.gis.db import models
from django_extensions.db.fields import AutoSlugField
from utils.fields import DictJSONField
from utils.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from=("name",),
        overwrite=False,
        editable=True,
        unique=True,
    )
    public_name = models.CharField(max_length=255)
    description_private = models.TextField(blank=True, null=True)
    description_public = models.TextField(blank=True, null=True)
    is_public_accessible = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    meta = DictJSONField(default=dict)
    group = models.ForeignKey(
        to="groups.Group",
        on_delete=models.SET_NULL,
        related_name="categories",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}, pk: {self.pk}"

    class Meta:
        abstract = False
        ordering = ("group__name", "name")
