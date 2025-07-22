from django.db import models


class Sex(models.TextChoices):
    M = "Male"
    F = "Female"
    L = "LGBTQ+"
