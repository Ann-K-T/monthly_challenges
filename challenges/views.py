from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# dictionary to hold monthly challenges
monthly_challenges = {
    "january": "Eat no meat for the whole month of January.",
    "february": "Walk 30 minutes every day in February.",
    "march": "Learn Django for the whole month of March.",
    "april": "Read 2 books in April.",
    "may": "Practice yoga every day in May.",
    "june": "Run 5km every day in June.",
    "july": "Drink 2 liters of water every day in July.",
    "august": "Write a blog post every week in August.",
    "september": "Learn a new language in September.",
    "october": "Complete a coding challenge every day in October.",
    "november": "Volunteer for a local charity in November.",
    "december": "Reflect on the year and set goals for December."
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This is not a valid month")
