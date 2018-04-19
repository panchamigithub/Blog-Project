from django.urls import path,re_path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('reg/',views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blog/',views.blogpost,name='blogpost'),
    path('viewblog/',views.viewblog,name='viewblog'),
    path('forgot/',views.security_question,name='security_question'),
    path('changep/',views.Password_change,name='Password_change'),
    re_path(r'edit/(?P<pk>[0-9]+)/$', views.editblog, name='editblog'),
    re_path(r'edit/(?P<pk>[0-9]+)/updateblog/$', views.updateblog, name='updateblog'),
]


