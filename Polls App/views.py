from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    questionn = Question.objects.all()
    return HttpResponse("<h1>Hello World!</h1>")
