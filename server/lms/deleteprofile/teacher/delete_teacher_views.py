
from django.http  import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  ...models  import TeacherProfile
from django.core.exceptions import ObjectDoesNotExist
import  redis
import  jwt
import  json
from django.conf import settings


r=redis.Redis(host='localhost',port=6379 ,  db=0)
@csrf_exempt
def  delete_teacher_profile(request):
    if request.method == 'POST':
        auth_header =  request.headers.get('Authorization')

        token = auth_header.split(' ')[1] if len(auth_header.split(' ')) == 2 else None
        if not token:
            return  JsonResponse({'message':'Invalid Authorization  error format ,  token  is not found'},status=404)
        
        try:
            decoded =  jwt.decode(token ,  settings.SECRET_KEY,algorithms=["HS256"])
            user_id =  decoded.get('user_id')

        except  jwt.ExpiredSignatureError:
            return JsonResponse({'message':'Jwt token has been expired'}, status=401)
        except  jwt.InvalidTokenError:
            return JsonResponse({'message':'Invalid token'}, status = 401)

        if not user_id:
            return  JsonResponse({'message':'Invalid token  payload, user_id is missing'}, status=400)

        try:
            techer_profile = TeacherProfile.objects.get(user_id=user_id)
            techer_profile.delete()

            cache_key =  f'teacher_profile_{user_id}'
            r.delete(cache_key)

            return  JsonResponse({'message':'Teacher profile deleted successfully'},status=200)

        except TeacherProfile.DoesNotExist:
            return  JsonResponse({'message':'Teacher profile does not exist'},status=404)

    return  JsonResponse({'Error':'Invalid Http  method only  Delete method is allowed'}, status=405)

        