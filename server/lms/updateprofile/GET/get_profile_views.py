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
def get_student_profile(request):
    if request.method == 'GET':
        # Extract JWT token from the Authorization header (Bearer token)
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'message': 'Authentication token not found in Authorization header'}, status=401)

        # Extract the token from 'Bearer <token>'
        token = auth_header.split(' ')[1] if len(auth_header.split(' ')) == 2 else None
        if not token:
            return JsonResponse({'message': 'Invalid Authorization format. Expected Bearer token.'}, status=400)

        try:
            # Decode the JWT token
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded.get("user_id")
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'Invalid token'}, status=401)

        if not user_id:
            return JsonResponse({'message': 'Invalid token payload: user_id missing'}, status=400)

        # Redis caching
        cache_key = f'student_profile_{user_id}'
        cached_profile = r.get(cache_key)

        if cached_profile:
            profile_data = json.loads(cached_profile)
            return JsonResponse({'student_profile': profile_data}, status=200)

        try:
            student_profile = StudentProfile.objects.get(user_id=user_id)
            profile_data = {
                'name': student_profile.name,
                'phone_number': student_profile.phone_number,
                'email': student_profile.email,
                'gender': student_profile.gender
            }
            r.set(cache_key, json.dumps(profile_data), ex=3600)
            return JsonResponse({'student_profile': profile_data}, status=200)

        except StudentProfile.DoesNotExist:
            return JsonResponse({'message': 'Student profile does not exist'}, status=404)

    return JsonResponse({"error": "Invalid HTTP method. Only GET allowed."}, status=405)
