from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views


urlpatterns =[  

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    
    path('',views.load_index,name='load_index'),
    path('enquery_send',views.enquery_send,name='enquery_send'),
   
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)