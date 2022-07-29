from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views


urlpatterns =[  
    
    path('',views.load_index,name='load_index'),
    path('load_about',views.load_about,name='load_about'),
    path('load_services',views.load_services,name='load_services'),
    path('load_course',views.load_course,name='load_course'),
    path('load_course_details',views.load_course_details,name='load_course_details'),
    path('load_contact',views.load_contact,name='load_contact'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)