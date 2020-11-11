from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    '''
    hello_world : returns HttpResponse
            Args:
                request : request_url
    '''
    return HttpResponse("Welcome To Blog Page")