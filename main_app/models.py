from django.db import models

# Create your models here.
class Celebrity(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    dob = models.CharField(max_length=50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']