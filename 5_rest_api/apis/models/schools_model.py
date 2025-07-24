from django.db import models


class Schools(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        unique_together = [["name", "abbreviation"]]
