
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import StudentProfile
from django.core.exceptions import ObjectDoesNotExist
import json
import redis
import  jwt
from django.conf import settings


r= redis.Redis(host='localhost', port=6379 ,  db=0)

   

@csrf_exempt
def update_student_profile(request):
    if request.method == 'POST':
        try:
            data =  json.loads(request.body)
            # user_id=   data.get('user_id')
            name =  data.get('name')
            phone_number= data.get('phone_number')
            email = data.get('email')
            gender=data.get('gender')
            
            if not all([name,email,phone_number,gender]):
                return  JsonResponse({'message':'All fields are required'},status=400)
            student_profile =  StudentProfile.objects.get(name=name)

            student_profile.name = name
            student_profile.phone_number=phone_number
            student_profile.email=email
            student_profile.gender=gender
            
            student_profile.save()
            cache_key  = f'student_profile_{student_profile.user_id}'
            r.delete(cache_key)
            return JsonResponse({'message':'Profile updated successfully'},status=200)

        except  ObjectDoesNotExist:
            return JsonResponse({'message':'Student profile does not exist'},status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    else:
        return JsonResponse({"error": "Invalid HTTP method."}, status=405)



