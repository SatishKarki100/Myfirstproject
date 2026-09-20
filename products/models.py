from django.db import models
from vendors.models import VendorStore

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    description=models.TextField()
    store=models.ForeignKey(VendorStore,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  

    REQUIRED_FIELDS=['name','price','description']