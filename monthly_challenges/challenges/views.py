from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#inside index() accept a parameter which will be passed in automatically into this function when it´s executed.
def index(request):

    # return here should be the response that is being sent back to the client
    # so to the browser, sending that request.
    return HttpResponse("This works!")
