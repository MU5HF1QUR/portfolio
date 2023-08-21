from django.shortcuts import render,HttpResponseRedirect
from . forms import  ContactForm
from . models import contactInfo

# Create your views here.

def ind (request):
    return render(request, 'App1/index.html')

def img (request):
    return render(request, 'App1/img.html')

def vid (request):
    return render(request, 'App1/vid.html')


def contactUs(request):
    frm = ContactForm(request.POST)
    if frm.is_valid():
        tname = frm.cleaned_data['name']
        temail = frm.cleaned_data['email']
        tphone = frm.cleaned_data['phone']
        tmessage = frm.cleaned_data['message']

        addToModel = contactInfo(name = tname, email = temail, phone = tphone, message = tmessage)
        addToModel.save()

        return HttpResponseRedirect('/')

    return render(request, 'App1/contact.html', {'form':frm})
