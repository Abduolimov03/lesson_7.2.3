from django.db import models

class AirPods(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.brand