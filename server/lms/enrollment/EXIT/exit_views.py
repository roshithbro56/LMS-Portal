
from  django.http  import  JsonResponse
from django.contrib.auth.decorators import login_required
from  ...models  import  StudentProfile,TeacherProfile
from  django.shortcuts import  get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def exit_from_teacher(request,teacher_id):
    student  =  get_object_or_404(StudentProfile,user=request.user)
    teacher=get_object_or_404(TeacherProfile,id=teacher_id)
    student.enrolled_teachers.remove(teacher)
    return  JsonResponse({'message':f"Exited from  {teacher.name}'s course"})