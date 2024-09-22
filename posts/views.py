from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse('<h1>Welcome to Django</h1>')


def home(request):

    return HttpResponse('<h3> Welcome to my site</h3>')

