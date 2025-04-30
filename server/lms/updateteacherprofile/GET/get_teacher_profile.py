
from  django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  ...models  import  TeacherProfile
from django.core.exceptions import ObjectDoesNotExist
import  redis
import  jwt
import  json
from django.conf import settings

r=redis.Redis(host='localhost' ,  port=6379 ,  db=0)
