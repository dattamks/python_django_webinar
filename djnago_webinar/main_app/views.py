from django.shortcuts import render
from .models import Contactform

# Create your views here.

def index(request):
    context = {}
    context['Message'] = 'Howdy!'
    context['name'] = 'Datakraft'

    return render(request,'index.html',context)


def contactform(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        new_message = Contactform(Name=name,Email=email,Subject=subject,Message=message)
        new_message.save()

    return render(request,'index.html')