from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send an email

        send_mail(
            'message from ' + name, # subject
            message, # message
            email, # from email
            ['zachjamescalo@gmail.com'], # to email

            )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blogsingle(request):
    return render(request, 'blog-single.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def index2(request):
    return render(request, 'index-2.html', {})

def portfoliodetails(request):
    return render(request, 'portfolio-details.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def services(request):
    return render(request, 'services.html', {})

def team(request):
    return render(request, 'team.html', {})
