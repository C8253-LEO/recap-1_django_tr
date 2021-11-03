from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .models import Teacher




# Create your views here.

def home(request):
    
    teachers = Teacher.objects.order_by("speciality").distinct()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been sent")
            return redirect("home")
    else:
        form = ContactForm()
        
    context = {
        'form':form, 
        "teachers":teachers
    }
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def teacher(request):
    teachers =Teacher.objects.all()
    
    context = {
        'teachers':teachers
    }
    
    return render(request, "home/teacher.html", context)