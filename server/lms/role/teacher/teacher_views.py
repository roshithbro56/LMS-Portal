
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from  ...models import  StudentProfile,TeacherProfile

        
@csrf_exempt
def create_teacher_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username =  data.get('username')
        name= data.get('name')
        subject =  data.get('subject')
        fees =  data.get('fees')
        duration = data.get('duration')
        
        try:
            user =  User.objects.get(username = username)
            if  hasattr(user , 'teacherprofile'):
                return JsonResponse({'error': 'Teacher profile already exists'}, status=400)

            TeacherProfile.objects.create(
                user=user,
                name=name,
                subject=subject,
                fees=fees,
                duration=duration
                
            )
            return JsonResponse({'message': 'Teacher profile created successfully'})
        except  User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

           
                
    
    

