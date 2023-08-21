from django.contrib.gis.db import models
from django_extensions.db.fields import AutoSlugField
from utils.fields import DictJSONField
from utils.models import BaseModel


class Group(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from=("name",),
        overwrite=False,
        editable=True,
        unique=True,
    )
    public_name = models.CharField(max_length=255)
    is_public_accessible = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    meta = DictJSONField(default=dict)

    def __str__(self) -> str:
        return f"{self.name}, pk: {self.pk}"

    class Meta:
        abstract = False
