from django.shortcuts import render, redirect
from .models import *



#Admin Section

def admin_dashboard(request):
    enquerys=Enquery.objects.all()
    return render(request,'Admin/index.html',{'enquerys':enquerys})


#Home Section

def load_index(request):
    return render(request,'User/index.html')

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
        return render(request,'home.html')