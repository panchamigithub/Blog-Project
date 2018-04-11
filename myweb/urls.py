from django.urls import path
from . import views

urlpatterns=[
    path('reg/',views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blog/',views.blogpost,name='blogpost'),
    path('index/',views.index,name='index'),
    path('viewblog/',views.viewblog,name='viewblog'),
    path('forgot/',views.security_question,name='security_question'),
    path('change_password/',views.Password_change,name='Password_change'),
]
