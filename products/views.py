from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Products


@login_required
def add_product(request):
    if request.user.role != 'vendor':
        messages.error(request, 'Only vendors can add products.')
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        price = request.POST.get('price', '').strip()
        image = request.FILES.get('image')

        errors = []
        if not name:
            errors.append('Name is required.')
        if not description:
            errors.append('Description is required.')
        if not price:
            errors.append('Price is required.')
        else:
            try:
                price = int(price)
                if price < 0:
                    errors.append('Price must be a positive number.')
            except ValueError:
                errors.append('Price must be a valid number.')

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'products/products.html', {
                'name': name,
                'description': description,
                'price': request.POST.get('price', ''),
            })

        product = Products(
            name=name,
            description=description,
            price=price,
            vendor=request.user,
        )
        if image:
            product.image = image
        product.save()
        return redirect('products:product-details', product_id=product.id)

    return render(request, 'products/products.html')


@login_required
def product_details(request, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'products/productdetails.html', {'product': product})
