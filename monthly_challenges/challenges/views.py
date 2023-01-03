from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.S

##inside index() accept a parameter which will be passed in automatically into this function when it´s executed.
#def january(request):

    ## return here should be the response that is being sent back to the client
    ## so to the browser, sending that request.
    #return HttpResponse("January no meat for the enire month!")

monthly_challenges = {
    "january": "January no meat for the entire month!",
    "february": "in February walk for at least 20 minutes every day!",
    "march": "March: Learn Django for at least 20 minutes every day!",
    "april": "April, Learn Django for at least 20 minutes every day!",
    "may": "May: Learn Django for at least 20 minutes every day!",
    "june": "January no meat for the entire month!",
    "july": "in February walk for at least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "no meat for the entire month!",
    "october": "walk for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "dicember": "no meat for the entire month!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported, not exist")

    redirect_month = months[month -1]

    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        #response_data = f"<h1>{challenge_text}</h1>"
        
        response_data = render_to_string("challenges/challenge.html")

        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
