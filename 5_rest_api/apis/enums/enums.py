from django.db import models


class Sex(models.TextChoices):
    M = "Man"
    W = "Woman"
    L = "LGBTQ+"
