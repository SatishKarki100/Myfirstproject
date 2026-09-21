from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        middlename = request.POST.get('middlename', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        role = request.POST.get('role', 'user')

        errors = []
        if not username:
            errors.append('Username is required.')
        if not first_name:
            errors.append('First name is required.')
        if not last_name:
            errors.append('Last name is required.')
        if not email:
            errors.append('Email is required.')
        if not password:
            errors.append('Password is required.')
        if password != password2:
            errors.append('Passwords do not match.')
        if role not in ['user', 'vendor']:
            errors.append('Invalid role.')
        if username and User.objects.filter(username=username).exists():
            errors.append('Username already taken.')
        if email and User.objects.filter(email=email).exists():
            errors.append('Email already registered.')

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'users/register.html', {
                'username': username,
                'first_name': first_name,
                'middlename': middlename,
                'last_name': last_name,
                'email': email,
                'role': role,
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middlename=middlename or None,
            role=role,
        )
        login(request, user)
        return redirect('profile')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request, 'Invalid username or password.')
        return render(request, 'users/login.html', {'username': username})

    return render(request, 'users/login.html')


@login_required(login_url='login')
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
