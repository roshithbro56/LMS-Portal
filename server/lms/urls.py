
from  django.urls import path
from  .auth.auth_views import register_user,login_user,logout_user
from   .role.role_views   import create_student_profile,create_teacher_profile
from  .student.student_views import get_teachers,search_teachers
from  .updateprofile.GET.get_profile_views import get_student_profile
from  .updateprofile.UPDATE.update_views import update_student_profile
from  .deleteprofile.delete_views  import delete_student_profile
urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
    
    # endpoints for the role selection
    path('profile/create-student-profile/', create_student_profile, name='create_student_profile'),
    path('profile/create-teacher-profile/', create_teacher_profile, name='create_teacher_profile'),
    
    #
    path('get-teachers/', get_teachers, name='get_teachers'),
    path('search-teachers/', search_teachers, name='search_teachers'),
    
    path('get-student-profile/', get_student_profile, name='get_student_profile'),
    path('update-student-profile/',update_student_profile, name='update_student_profile'),
    
    # delete student profile 
    path('delete-student-profile/', delete_student_profile,name='delete_profile')

]
