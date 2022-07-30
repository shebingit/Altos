from django.shortcuts import render



#Admin Section

def admin_dashboard(request):
    return render(request,'Admin_Dasbord.html')


#Home Section

def load_index(request):
    return render(request,'index.html')

def load_about(request):
    return render(request,'about.html')

def load_services(request):
    return render(request,'services.html')

def load_course(request):
    return render(request,'course.html')

def load_course_details(request):
    return render(request,'course-details.html')

def load_contact(request):
    return render(request,'contact.html')

