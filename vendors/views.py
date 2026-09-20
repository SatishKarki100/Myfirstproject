from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import VendorStore


@login_required
def register_vendorstore(request):
    if request.method == 'POST':
        store_name = request.POST.get('store_name', '').strip()
        description = request.POST.get('description', '').strip()
        business_email = request.POST.get('business_email', '').strip()

        errors = []
        if not store_name:
            errors.append('Store name is required.')
        if not description:
            errors.append('Description is required.')
        if not business_email:
            errors.append('Business email is required.')

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'vendors/register.html', {
                'store_name': store_name,
                'description': description,
                'business_email': business_email,
            })

        vendor = VendorStore(
            user=request.user,
            store_name=store_name,
            description=description,
            business_email=business_email,
        )
        vendor.save()
        return redirect('store', store_id=vendor.id)

    return render(request, 'vendors/register.html')


@login_required
def store_view(request, store_id):
    store = VendorStore.objects.get(id=store_id)
    return render(request, 'vendors/store.html', {
        'title': 'Your Store',
        'store': store,
    })
