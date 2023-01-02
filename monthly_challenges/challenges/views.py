from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.S

##inside index() accept a parameter which will be passed in automatically into this function when it´s executed.
#def january(request):

    ## return here should be the response that is being sent back to the client
    ## so to the browser, sending that request.
    #return HttpResponse("January no meat for the enire month!")



def monthly_challenges(request, month):

    challenge_text = None

    if month == 'january':
        challenge_text = "January no meat for the entire month!"

    elif month == "february":
        challenge_text = "in February walk for at least 20 minutes every day!"

    elif month == "march":
        challenge_text = "March: Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)