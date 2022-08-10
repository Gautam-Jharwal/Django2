from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(requests):
    context = {
        'variable':'this is sent'
    }
    return render(requests,'index.html',context)
    #return HttpResponse('This is Home Page')

def about(requests):
    return render(requests,'About.html')

def services(requests):
    return render(requests,'Services.html')
def Contacts(requests):
    return render(requests,'Contact.html')