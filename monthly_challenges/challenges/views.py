from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.S

#inside index() accept a parameter which will be passed in automatically into this function when it´s executed.
def january(request):

    # return here should be the response that is being sent back to the client
    # so to the browser, sending that request.
    return HttpResponse("January no meat for the enire month!")


def february(request):

    return HttpResponse('in February walk for at least 20 minutes every day!')


def march(request):

    return HttpResponse("March: Learn Django for at least 20 minutes every day!")
