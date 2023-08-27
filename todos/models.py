from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=250)
    date_do = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
