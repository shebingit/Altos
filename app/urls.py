from django.views import *
from django.urls import  path,reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views


urlpatterns =[  

    path('load_login',views.load_login,name='load_login'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    #==========password change==========
    path('account_password',views.account_password,name='account_password'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='Admin/account_password.html',success_url=reverse_lazy('password_change_done')), 
                name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Admin/password_change_done.html'), 
                name='password_change_done'),

                

    #======Admin===============


    path('load_dashbord',views.load_dashbord,name='load_dashbord'),
    path('load_addsection',views.load_addsection,name='load_addsection'),
    path('enquery_delete/<int:enq_delete_id>',views.enquery_delete,name='enquery_delete'),
    path('projectenq_delete/<int:enqproject_delete_id>',views.projectenq_delete,name='projectenq_delete'),




    #=============User===============

    
    path('',views.load_index,name='load_index'),
    path('training_load',views.training_load,name='training_load'),
    path('mail_send',views.mail_send,name='mail_send'),
    path('enquery_send',views.enquery_send,name='enquery_send'),
    path('project_enquery_send',views.project_enquery_send,name='project_enquery_send'),
   
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)