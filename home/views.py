from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error404(request,exception):
    return render(request, 'pages/error.html')
def error500(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST': #and form.is_valid()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'pages/register.html', {'form': form})

