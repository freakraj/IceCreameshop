from django.shortcuts import render ,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
          "variable1":"Raj Gautam your best Dajango Developer",
          "variable2" : "Rohit is a good MVC developer"
    }

    return render(request, 'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
     return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
     return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            desc = request.POST.get('desc')
            contact = Contact(name=name , phone=phone , email=email , desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Your Msg Has Been sent')
        return render(request, 'contact.html')
         

    # return HttpResponse("this is contact page ")