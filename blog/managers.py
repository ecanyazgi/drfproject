from django.db import models
from . import enums

class PostQuerySet(models.QuerySet):
    def get_queryset(self):
        return super().get_queryset().filter(status=enums.Options.PUBLISHED)
