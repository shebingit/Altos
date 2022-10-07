import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import *



# 404 Page not found
def handle_not_found(request,exception):
    return render(request,'User/PageNotFound.html')

#Home Section

def load_index(request):
    clients=Clients.objects.all()
    projects=OnProjects.objects.all()
    return render(request,'User/index.html',{'projects':projects,'clients':clients})

def load_about(request):
    clients=Clients.objects.all()
    projects=OnProjects.objects.all()
    return render(request,'User/index.html',{'projects':projects,'clients':clients})


def training_load(request):
    courses=Courses.objects.all()
   
    return render(request,'User/Training.html',{'courses':courses})


def enquery_send(request):
    
   if request.method=="POST":
        cname=request.POST['coname']
        cour_id=Courses.objects.get(course_name=cname)
        fname=request.POST['fname']
        locality=request.POST['place']
        phno=request.POST['phno']
        email=request.POST['emailid']
        enq=Enquery(name=fname,
                    email=email,
                    contact=phno,
                    place=locality,
                    course_id=cour_id)
        enq.save()
        message="Our Training Team Will Contact You Soon ."
        courses=Courses.objects.all()
        return render(request,'User/Training.html',{'message':message,'courses':courses})

def project_enquery_send(request):
    fname=request.POST['pfname']
    msgs=request.POST['msg']
    phno=request.POST['pphno']
    email=request.POST['pemailid']
    project_enq=Project_Enquery(enq_name=fname,
                    enq_email=email,
                    enq_contact=phno,
                    enq_project='',
                    enq_message=msgs)
    project_enq.save()
    message="Thank you ! Admin will respond soon"
    return render(request,'User/index.html',{'message':message})






#===============Admin side====================


def load_login(request):
    return render(request,'Admin/login.html')

def account_password(request):
    return render(request,'Admin/account_password.html')

def login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id

                if user is not None:
                    auth.login(request, user)
                    if user.is_superuser==1:
                        
                        enquerys=Enquery.objects.all()
                        pro_enquerys=Project_Enquery.objects.all()
                        message=None
                        return render(request,'Admin/index.html',{'enquerys':enquerys,'pro_enquerys':pro_enquerys})
                        
                    else:
                        message='Invalid username or password'
                        return render(request,'Admin/login.html',{'message':message})
            except:
                message='Invalid username or password'
                return render(request,'Admin/login.html',{'message':message})                       
        else:
            #messages.info(request, 'Invalid username or password')
            message='Invalid username or password'
            return render(request,'Admin/login.html',{'message':message})
                   
    except:
       # messages.info(request, 'Invalid username or password')
        message='Invalid username or password'
        return render(request,'Admin/login.html',{'message':message})


@login_required(login_url="/load_login")
def load_dashbord(request):
    enquerys=Enquery.objects.all()
    pro_enquerys=Project_Enquery.objects.all()
   
    return render(request,'Admin/index.html',{'enquerys':enquerys,'pro_enquerys':pro_enquerys})


@login_required(login_url="/load_login")
def load_addsection(request):
    courses=Courses.objects.all()
    clients=Clients.objects.all()
    projects=OnProjects.objects.all()
    return render(request,'Admin/Addsection.html',{'courses':courses,'projects':projects,'clients':clients})

def enquery_delete(request,enq_delete_id):
    enquery=Enquery.objects.get(id=enq_delete_id)
    enquery.delete()
    msg="Deleted Successfuly."
    enquerys=Enquery.objects.all()
    pro_enquerys=Project_Enquery.objects.all()
    return render(request,'Admin/index.html',{'enquerys':enquerys,'pro_enquerys':pro_enquerys,'msg':msg})

def projectenq_delete(request,enqproject_delete_id):
    enquery=Project_Enquery.objects.get(id=enqproject_delete_id)
    enquery.delete()
    msg="Deleted Successfuly."
    enquerys=Enquery.objects.all()
    pro_enquerys=Project_Enquery.objects.all()
    return render(request,'Admin/index.html',{'enquerys':enquerys,'pro_enquerys':pro_enquerys,'msg':msg})


def add_course(request):
    if request.method=="POST":
        
        cname=request.POST['cname']
        cdis=request.POST['cdiscription']
        cimg=request.FILES.get('cimage')
        course=Courses(course_name=cname,
                        course_discr=cdis,
                        course_img=cimg)
        course.save()
        messages="Courses Successfully Added."
        courses=Courses.objects.all()
        return render(request,'Admin/Addsection.html',{'courses':courses,'messages':messages,'c_name':cname})

    else:
        return(request,'Admin/Addsection.html')
    

def add_project(request):
    if request.method=="POST":
        
        pname=request.POST['pname']
        pdis=request.POST['pdiscription']
        pimg=request.FILES.get('pimage')
        project=OnProjects(project_name=pname,
                        project_discr=pdis,
                        project_img=pimg)
        project.save()
        messages="Project Successfully Added."
        projects=OnProjects.objects.all()
        return render(request,'Admin/Addsection.html',{'projects':projects,'messages':messages,'proje_name':pname})

    else:
        return(request,'Admin/Addsection.html')


def add_clients(request):
    if request.method=="POST":
        
        clname=request.POST['clname']
        cldis=request.POST['cldiscription']
        climg=request.FILES.get('clogo')
        client=Clients(client_name=clname,
                        client_discr=cldis,
                        client_logo=climg)
        client.save()
        messages="Client Successfully Added."
        clients=Clients.objects.all()
        return render(request,'Admin/Addsection.html',{'clients':clients,'messages':messages,'client_name':clname})

    else:
        return(request,'Admin/Addsection.html')




#admin side update section

def load_update(request,up_id, setionid):
    if setionid == 1:
        data=Courses.objects.get(id=up_id)
        value=1
    elif  setionid == 2:
        data=OnProjects.objects.get(id=up_id)
        value=2
    else:
        data=Clients.objects.get(id=up_id)
        value=3

    return render(request,'Admin/Updatesection.html',{'data':data,'value':value})



def updatesetions(request,updateid, upsectionid):

    if upsectionid == 1:
        if request.method=="POST":
            data=Courses.objects.get(id=updateid)
            data.course_name=request.POST.get('cname')
            data.course_discr=request.POST.get('cdiscription')
            img=request.FILES.get('cimage')
            if(img):
                data.course_img=img
            else:
                data.course_img=data.course_img
            data.save()
            return redirect('load_addsection')
        
        
    elif  upsectionid == 2:
        if request.method=="POST":
            data=OnProjects.objects.get(id=updateid)
            data.project_name=request.POST.get('pname')
            data.project_discr=request.POST.get('pdiscription')
            img=request.FILES.get('pimage')
            if(img):
               data.project_img=img
            else:
               data.project_img=data.project_img
            data.save()
            return redirect('load_addsection')

      
    else:
        if request.method=="POST":
            data=Clients.objects.get(id=updateid)
            data.client_name=request.POST.get('clname')
            data.client_discr=request.POST.get('cldiscription')
            img=request.FILES.get('clogo')
            if(img):
              data.client_logo=img
            else:
              data.client_logo=data.client_logo
            data.save()
            return redirect('load_addsection')
       


#admin side delete section 

def course_delete(request,coursedelete_id):
    courses=Courses.objects.get(id=coursedelete_id)
    c_name=courses.course_name
    courses.delete()
    messages="Record Deleted."
    courses=Courses.objects.all()
    return render(request,'Admin/Addsection.html',{'courses':courses,'c_name':c_name,'messages':messages})

def project_delete(request,projectdelete_id):
    project=OnProjects.objects.get(id=projectdelete_id)
    p_name=project.project_name
    project.delete()
    messages="Record Deleted."
    projects=OnProjects.objects.all()
    return render(request,'Admin/Addsection.html',{'projects':projects,'proje_name':p_name,'messages':messages})


def client_delete(request,clientdelete_id):
    client=Clients.objects.get(id=clientdelete_id)
    cl_name=client.client_name
    client.delete()
    messages="Record Deleted."
    clients=Clients.objects.all()
    return render(request,'Admin/Addsection.html',{'clients':clients,'client_name':cl_name,'messages':messages})


def mail_send(request):
    msg="Mail sended."
    return render(request,'User/index.html',{'msg':msg})


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('load_index')