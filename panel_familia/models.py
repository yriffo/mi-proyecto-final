from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id}, {self.name}"
