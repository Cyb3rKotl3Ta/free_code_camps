from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [123, 456, 789]
    }
    return render(request, 'about.html', my_context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})