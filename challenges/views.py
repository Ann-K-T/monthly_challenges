from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the whole month of January."
    elif month == "february":
        challenge_text = "Walk 30 minutes every day in February."
    else:
        return HttpResponseNotFound("Please select a valid month.")
    return HttpResponse(challenge_text)
