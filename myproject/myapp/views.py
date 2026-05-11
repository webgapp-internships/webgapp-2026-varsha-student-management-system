from django.shortcuts import render

# Create your views here.
def index(request):
    varsha="full stack development "
    return render(request,"main.html",{'varsha':varsha})

def about(request):
    about="this page of about"
    return render(request,"about.html",{'about':about})

def contact(request):
    contact="this page is contact page "
    return render(request,"contact.html",{'contact':contact})

def services(request):
    services="this page is for services"
    return render(request,"services.html",{'services':services})

def form(request):
    return render(request,"form.html")

def table(request):
    return render(request,"table.html")

def testing(request):
    return render(request,"testing.html")

def webpage(request):
    return render(request, 'webpage.html')