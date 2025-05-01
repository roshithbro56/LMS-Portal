
from  django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  ...models  import  TeacherProfile
from django.core.exceptions import ObjectDoesNotExist
import  redis
import  jwt
import  json
from django.conf import settings
import decimal

r=redis.Redis(host='localhost' ,  port=6379 ,  db=0)
def convert_decimal_to_float(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

@csrf_exempt 
def get_teacher_profile(request):
    
    if request.method == 'GET':
        auth_header =  request.headers.get('Authorization')
        if not  auth_header:
            return JsonResponse({'message':'Authorization  token  not  found'},status=401)

        token = auth_header.split(' ')[1] if len(auth_header.split(' ')) == 2 else None
        if not token:
            return  JsonResponse({'message':'Invalid Authorization format.Expected bearer token'},status=400)

        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id =  decoded.get('user_id')
        except jwt.ExpiredSignatureError:
            return  JsonResponse({'message':'Jwt token has been  expired'}, status = 401)

        except  jwt.InvalidTokenError:
            return  JsonResponse({'message':'Invalid jwt token'}, status = 401)

        if not user_id:
            return JsonResponse({'message':'Invalid token payload , user_id  is missing '}, status = 400)
        
        cache_key =  f'teacher_profile_{user_id}'
        cache_profile =  r.get(cache_key)
        if cache_profile:
            profile_data = json.loads(cache_profile)
            return  JsonResponse({'teacher profile': profile_data},status=200)
        
        try:
            teacher_profile =  TeacherProfile.objects.get(user_id=user_id)
            profile_data = {
                'name':teacher_profile.name,
                'subject':teacher_profile.subject,
                'fees': convert_decimal_to_float(teacher_profile.fees),
                'duration':teacher_profile.duration
            }
            r.set(cache_key ,  json.dumps(profile_data),ex=3600) #caching for one hour 
            return JsonResponse({'teacher_profile':profile_data},status=200)
        except  TeacherProfile.DoesNotExist:
            return  JsonResponse({'message':'Teacher profile does not exist'}, status = 404)

        
    return  JsonResponse({'message':'Invalid Http method , only GET method is allowed'}, status =405)

        

