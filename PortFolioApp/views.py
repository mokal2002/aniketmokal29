from pyexpat.errors import messages
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib import messages
from .models import Contact, Feedback,  MySkills, MyPortfolio

# Create your views here.
def index(request):
    skills = MySkills.objects.all()
    portfolio = MyPortfolio.objects.all()
    return render(request, 'index.html', {'skills': skills, 'portfolio': portfolio})




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = request.POST.get('date')
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message, date=date)
        contact.save()
        messages.success(request, " Your message was sent...")
        return redirect('/contact/')

    
    return render(request, 'contact.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('femail')
        review = request.POST.get('freview')
        submit = Feedback(name=name, email=email, review=review)
        submit.save()
        messages.success(request, " Your message was sent...")
        return redirect('/feedback/')
    
    return render(request, 'feedback.html')
    