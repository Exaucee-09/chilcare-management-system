from django.db import models
from datetime import date

# Create your models here.
class Child (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=False, default=date(2005, 1, 1))
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.date_of_birth} {self.guardian_name} {self.guardian_contact} {self.address} "
