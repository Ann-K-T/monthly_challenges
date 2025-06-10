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
    "june": "Run 5km every day in June.",
    "july": "Drink 2 liters of water every day in July.",
    "august": "Write a blog post every week in August.",
    "september": "Learn a new language in September.",
    "october": "Complete a coding challenge every day in October.",
    "november": "Volunteer for a local charity in November.",
    "december": "Reflect on the year and set goals for December."
}


def index(request):
    # create empty string to hold list items
    list_items = ""
    # get the keys of the dictionary which are the months and convert them to a list
    months = list(monthly_challenges.keys())

    # iterate through list of months and create list items with links
    for month in months:
        capitalized_month = month.capitalize()
        # use reverse to get the URL for the month challenge
        month_path = reverse("month-challenge", args=[month])
        # append the list item to the list_items string to create a list of links of months
        list_items += f"<li><a href=\"{month_path}\"> {capitalized_month}</a></li>"
    # wrap the list items in an unordered list and return as HttpResponse
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not a valid month </h1>")
