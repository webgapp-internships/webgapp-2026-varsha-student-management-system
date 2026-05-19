from django.shortcuts import render, redirect
from .models import Student

def index(request):
    varsha = "full stack development "
    return render(request, "main.html", {'varsha': varsha})


def about(request):
    about = "this page of about"
    return render(request, "about.html", {'about': about})


def contact(request):
    contact = "this page is contact page "
    return render(request, "contact.html", {'contact': contact})


def services(request):
    services = "this page is for services"
    return render(request, "services.html", {'services': services})


def form(request):
    return render(request, "form.html")


def table(request):
    return render(request, "table.html")


def testing(request):
    return render(request, "testing.html")


def webpage(request):
    return render(request, 'webpage.html')


def taskweb(request):
    return render(request, 'taskweb.html')


def food1(request):
    return render(request, 'food1.html')


def food2(request):
    return render(request, 'food2.html')


def food3(request):
    return render(request, 'food3.html')

def stdform(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        address = request.POST.get('address')

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            department=department,
            address=address
        )

        return redirect('result')
    return render(request, 'stdform.html')

def result(request):
    result = Student.objects.all()
    return render(request, 'result.html', {"result": result})

def edit(request, id):

    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.gender = request.POST.get('gender')
        student.department = request.POST.get('department')
        student.address = request.POST.get('address')
        student.save()
        return redirect('result')

    return render(request, 'edit.html', {'student': student})

def website(request):
    return render(request, "website.html")

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('result')