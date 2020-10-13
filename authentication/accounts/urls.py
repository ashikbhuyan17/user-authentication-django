from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher_register/', views.teacher_reg_view, name='teacher_reg'),
    path('student_register/', views.student_reg_view, name='student_reg'),
    path('teacher_login/', views.teacher_login_view, name='teacher_login'),
    path('student_login/', views.student_login_view, name='student_login'),
    path('student_login/dashboard/',views.dashboard,name='student_dashboard'),
    path('teacher_login/dashboard/',views.dashboard,name='dashboard')
    ]