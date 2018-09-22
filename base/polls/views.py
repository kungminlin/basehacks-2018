from django.shortcuts import render

# Create your views here.
import os
from lxml import html
from django.http import HttpResponse


def index(request):
    str = "Error."
    with open(os.getcwd() + r'\public\index.html', "r") as f:
        str = f.read()
    return HttpResponse(str)
