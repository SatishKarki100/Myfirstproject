from django.db import models
from django.conf import settings


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='products',null=True,blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
