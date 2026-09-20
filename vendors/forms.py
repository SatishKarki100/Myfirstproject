from django import forms
from .models import VendorStore

class VendorStoreForm(forms.ModelForm):
    class Meta:
        model = VendorStore
        fields = ['store_name', 'description', 'business_email']
