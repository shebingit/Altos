from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import *



#Admin Section

def admin_dashboard(request):
    enquerys=Enquery.objects.all()
    return render(request,'Admin/index.html',{'enquerys':enquerys})


#Home Section

def load_index(request):
    return render(request,'User/index.html')

def training_load(request):
    return render(request,'User/Training.html')


def enquery_send(request):
    
   if request.method=="POST":
        fname=request.POST['fname']
        locality=request.POST['place']
        phno=request.POST['phno']
        email=request.POST['emailid']
        enq=Enquery(name=fname,
                    email=email,
                    contact=phno,
                    place=locality)
        enq.save()
        message="Successfully Registered ."
        return render(request,'User/Training.html',{'message':message})

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
    message="Thank you ! We will respond soon"
    return render(request,'User/index.html',{'message':message})






#===============Admin side====================


def load_login(request):
    return render(request,'Admin/login.html')



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


def mail_send(request):
    msg="Mail sended."
    return render(request,'User/index.html',{'msg':msg})


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('load_index')