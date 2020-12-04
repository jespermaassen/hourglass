from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():

            size = form.cleaned_data['size']

            print(size)

    form = ContactForm()
    return render(request, 'playground/index.html', context={'form': form})
