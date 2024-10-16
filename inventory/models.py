from django.db import models

class Asset(models.Model):
    asset_type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    last_maintenance = models.DateField()
    status = models.CharField(max_length=20)
    specifications = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.model})"
