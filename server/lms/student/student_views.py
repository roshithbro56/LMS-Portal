
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import redis
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from  ..models import  TeacherProfile

#setup  redis connection 
r=  redis.Redis(host='localhost',port=6379, db=0)

@csrf_exempt
def get_teachers(request):
    if request.method == 'GET':
        cahced_teachers =  r.get('teachers_list')

        if cahced_teachers:
            teachers =  json.loads(cahced_teachers)
            return  JsonResponse({'teacher':teachers},safe=False)

        else:
            teachers =  TeacherProfile.objects.all().values('name','subject','duration','fees')
            teachers_list = []
            for teacher in  teachers:
                teachers_list.append({
                    
                    'name':teacher['name'],
                    'subject':teacher['subject'],
                    'fees':str(teacher['fees']),
                    'duration':teacher['duration']
                })
            r.set('teachers_list', json.dumps(teachers_list),ex=3600)

            return  JsonResponse({'teacher':teachers_list},safe=False)
        

@csrf_exempt
def search_teachers( request ):
    if request.method == 'GET':
        subject  =  request.GET.get('subject') #getting the subject param from the url  
        if not subject:
            return  JsonResponse({'error':'subject parameter is  required'}, status = 400)

        cache_key =  f'teachers_search_{subject.lower()}'
        cached_teachers =  r.get(cache_key)

        if cached_teachers:
            teachers  =  json.loads(cached_teachers)
            return JsonResponse({'teacher':teachers},safe=False)
        
        else:
            teachers  = TeacherProfile.objects.filter(subject__icontains= subject).values('name', 'subject', 'duration', 'fees')
            teachers_list = []
            for teacher  in teachers:
                teachers_list.append({
                    'name':teacher['name'],
                    'subject':teacher['subject'],
                    'fees':str(teacher['fees']),
                    'duration':teacher['duration']
                    
                })
                
            r.set(cache_key,json.dumps(teachers_list),ex=3600)
            return JsonResponse({'teacher': teachers_list}, safe=False)
