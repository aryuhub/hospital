from django.shortcuts import render
from .models import Departments,Doctors,About
from .forms import BookingForm

# Create your views here.

def index(request):

    return render(request ,'index.html')

def about(request):
    pro = {'profile':About.objects.all()}
    return render(request,'about.html',pro)

def appointment(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form = {'form':form}
    return render(request,'appointment.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dep = {'dept': Departments.objects.all() }
    return render(request,'department.html',dict_dep)