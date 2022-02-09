from django.db import models

class Options(models.TextChoices):
    DRAFT = 'draft'
    PUBLISHED = 'published'