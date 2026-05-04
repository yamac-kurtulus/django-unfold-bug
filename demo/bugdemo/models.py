from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=100)
    filter_date = models.DateField()
    editable_date = models.DateField()

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title
