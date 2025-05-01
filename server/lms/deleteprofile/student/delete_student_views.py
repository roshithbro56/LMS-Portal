

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...models import StudentProfile
from django.core.exceptions import ObjectDoesNotExist
import json
import redis
import  jwt
from django.conf import settings

r=redis.Redis(host='localhost',port=6379 ,  db=0)
@csrf_exempt
def  delete_student_profile(request):
    if request.method == 'DELETE':
        auth_header =  request.headers.get('Authorization')
        if not  auth_header:
            return  JsonResponse({'message':'Authorization  token  is not  found'})

        token = auth_header.split(' ')[1] if len(auth_header.split(' ')) == 2 else None
        if not token:
            return JsonResponse({'message': 'Invalid Authorization format. Expected Bearer token.'}, status=400)
        
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id =  decoded.get('user_id')

        except jwt.ExpiredSignatureError:
            return  JsonResponse({'message':'Token  has expired'}, status=401)
        except jwt.InvalidTokenError:
            return  JsonResponse({'message':'Invalid token'},status=401)
        
        if not user_id:
            return JsonResponse({'message':'user id is not found in that payload'}, status=400)

        try:
            student_profile =  StudentProfile.objects.get(user_id=user_id)
            student_profile.delete()

            cache_key =  f'student_profile_{user_id}'
            r.delete(cache_key)
            
            return  JsonResponse({'message':'Student profile deleted successfully'}, status =200)

        except StudentProfile.DoesNotExist:
            return  JsonResponse({'message':'Student profile does not exist'}, status= 404)

    return  JsonResponse({'message':'Invalid Http response only  DELETE method is allowed'},status=405)
            
            

