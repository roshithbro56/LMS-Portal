from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from  ...models import  StudentProfile


@csrf_exempt
def create_student_profile(request):
    if  request.method == 'POST':
        data =  json.loads(request.body)
        username  =  data.get('username')
        name= data.get('name')
        phone_number=  data.get('phone_number')
        email =  data.get('email')
        gender= data.get('gender')
        print(username,email,phone_number,gender,name)

        try:
            user =  User.objects.get(username = username)
            if hasattr(user ,  'studentprofile'):
                return JsonResponse({'error': 'Student profile already exists'}, status=400)
            StudentProfile.objects.create(
                
                user=user,
                name=name,
                phone_number=phone_number,
                email=email,
                gender=gender
            )
            return JsonResponse({'message': 'student profile  created successfully'})
        
        except  User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)