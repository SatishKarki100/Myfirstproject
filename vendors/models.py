from django.db import models
from users.models import User
from django.utils.text import slugify
# Create your models here.

class VendorStore(models.Model):
    user=models.ForeignKey(User,verbose_name=('vendor_user'),on_delete=models.CASCADE,related_name='stores')
    store_name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    business_email=models.EmailField()
    

    REQUIRED_FIELDS = ['store_name','description', 'business_email']  
        
    def __str__(self):
        return self.store_name
