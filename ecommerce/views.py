from django.shortcuts import render
from products.models import Products

def home_view(request):

    all_products = Products.objects.all() 
    
    context = {
        'products': all_products
    }
    return render(request, 'main/home.html', context=context)