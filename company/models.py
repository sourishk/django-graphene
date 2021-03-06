# File contains the model definitions.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_info = models.CharField(max_length=200)
    employee_size = models.PositiveIntegerField()

    def __str__(self):
        return self.name