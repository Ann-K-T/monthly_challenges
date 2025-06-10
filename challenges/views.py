from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat healthy food.")


def february(request):
    return HttpResponse("Walk 30min everyday.")
