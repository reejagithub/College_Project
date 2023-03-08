from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.base,name='base'),
    path('add_course',views.add_course,name='add_course'),
    path('course_db',views.course_db,name='course_db'),
    path('log_in',views.log_in,name='log_in'),
    path('signup',views.signup,name='signup'),
    path('user',views.user,name="user"),
    path('login_in/',views.login_in,name="login_in"),
    path('admin',views.admin,name='admin'),
    path('add_stud',views.add_stud,name="add_stud"),
    path('stud_db',views.stud_db,name='stud_db'),
    path('show_details',views.show_details,name="show_details"),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_db/<int:pk>',views.edit_db,name='edit_db'),
    path('delt/<int:pk>',views.delt,name='delt'),

#LOGOUT

    path('logout',views.logout,name='logout'),

    #teacher
   
    path('tsignup',views.tsignup,name='tsignup'),
    path('tuser',views.tuser,name='tuser'),
    
  

    #see  teacher profile url
    path('profile',views.profile,name='profile'),
    path('welcome',views.welcome,name='welcome'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    #show teacher profile url
    path('showt_details',views.showt_details,name='showt_details'),
    #edit teacher
    path('profile_edit',views.profile_edit,name='profile_edit'),
    
    path('Del/<int:pk>',views.Del,name='Del')
   
    
]
