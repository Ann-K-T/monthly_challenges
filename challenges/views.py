from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# dictionary to hold monthly challenges
monthly_challenges = {
    "january": "Eat no meat for the whole month of January.",
    "february": "Walk 30 minutes every day in February.",
    "march": "Learn Django for the whole month of March.",
    "april": "Read 2 books in April.",
    "may": "Practice yoga every day in May.",
    "june": None,
    "july": "Drink 2 liters of water every day in July.",
    "august": "Write a blog post every week in August.",
    "september": "Learn a new language in September.",
    "october": "Complete a coding challenge every day in October.",
    "november": "Volunteer for a local charity in November.",
    "december": None
}

##################################################


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


##################################################

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

##################################################


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This is not a valid month </h1>")
