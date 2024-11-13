from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.role} {self.contact} {self.hire_date}"