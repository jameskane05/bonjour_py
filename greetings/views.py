from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    lang = request.GET.get('lang')
    greeting = Greeting.objects.get(language__exact=lang) # get the language field that's exactly the same as lang
    # referring to .objects is a way of getting data out of the object
    return HttpResponse(greeting.text + ', Django!')