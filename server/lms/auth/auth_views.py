
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
def register_user(request):
    
    if request.method == 'POST':
        data =  json.loads(request.body)
        username  =  data.get('username')
        email = data.get('email')
        password= data.get('password')

        if not username or not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        User.objects.create_user(username=username,email=email,password=password)
        return JsonResponse({'message': 'User registered successfully'})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        print(f"Attempting login with username: {username}, password: {password}")  # Debugging line

        user = authenticate(username=username, password=password)
        print(f"{user} ")

        if user is not None:
            print(f"User authenticated: {user}")  # Debugging line
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'Login successful',
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        else:
            print(f"Authentication failed for username: {username}")  # Debugging line
            return JsonResponse({'error': 'Login Failed'}, status=401)

    return JsonResponse({'error': 'Invalid credentials'}, status=401)


@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'})


           