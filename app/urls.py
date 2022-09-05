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

    #====Add Section=========

    path('add_course',views.add_course,name='add_course'),
    path('add_project',views.add_project,name='add_project'),
    path('add_clients',views.add_clients,name='add_clients'),


    #=====Delete Section=======

    path('course_delete/<int:coursedelete_id>',views.course_delete,name='course_delete'),
    path('project_delete/<int:projectdelete_id>',views.project_delete,name='project_delete'), 
    path('client_delete/<int:clientdelete_id>',views.client_delete,name='client_delete'), 

    #===== Update Section=======

    path('load_update/<int:up_id>/<int:setionid>',views.load_update,name='load_update'),
    path('updatesetions/<int:updateid>/<int:upsectionid>',views.updatesetions,name='updatesetions'),



    #=============User===============

    
    path('',views.load_index,name='load_index'),
    path('load_about',views.load_about,name='load_about'),
    path('training_load',views.training_load,name='training_load'),
    path('mail_send',views.mail_send,name='mail_send'),
    path('enquery_send',views.enquery_send,name='enquery_send'),
    path('project_enquery_send',views.project_enquery_send,name='project_enquery_send'),
   
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)