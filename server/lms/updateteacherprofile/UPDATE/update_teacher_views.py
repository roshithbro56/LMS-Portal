
from  django.http  import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  ...models  import  TeacherProfile
from django.core.exceptions import ObjectDoesNotExist
import  redis
import jwt
import  json
from  django.conf import  settings

r= redis.Redis(host='localhost',port= 6379 , db=0)
@csrf_exempt
def update_teacher_profile(request):
    if request.method ==  'POST':
        try:
            data =  json .loads(request.body)
            auth_header=  request.headers.get('Authorization')
            if not  auth_header:
                return  JsonResponse({'message':'Authorization  token is not found'},status=401)
            token = auth_header.split(' ')[1] if len(auth_header.split(' ')) == 2 else None
            if not token:
                return   JsonResponse({'message':'Invalid Authorization  token ,expection  beare token'},status=400)

            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id =  decoded.get('user_id')
            except  jwt.ExpiredSignatureError:
                return JsonResponse({'message':'token  is expired'},status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'message': 'Invalid token'}, status=401)

            if not user_id:
                return  JsonResponse({'message':'User id is not found  in the payload'},status=400)
            
            name =data.get('name')
            fees=data.get('fees')
            subject=data.get('subject')
            duration=data.get('duration')
            
            if not all([name,fees,subject,duration]):
                return JsonResponse({'message':'All fields are required'},status=400)

            teacher_profile =  TeacherProfile.objects.get(user_id=user_id)
            teacher_profile.name= name
            teacher_profile.fees =  fees
            teacher_profile.duration=duration
            teacher_profile.subject=subject
            teacher_profile.save()
            cahce_key= f"teacher_profile_{user_id}"
            r.delete(cahce_key)

            return JsonResponse({'message': 'Profile updated successfully'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Teacher profile does not exist'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    return JsonResponse({"error": "Invalid HTTP method. Only POST allowed."}, status=405)


        