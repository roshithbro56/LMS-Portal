

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from  ...models  import  StudentProfile,TeacherProfile
from  django.shortcuts import  get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_in_teacher(request, teacher_id):
    student = get_object_or_404(StudentProfile, user=request.user)
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)
    student.enrolled_teachers.add(teacher)
    return Response({"message": f"Enrolled in {teacher.name}'s course."})