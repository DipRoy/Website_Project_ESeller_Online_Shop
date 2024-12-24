from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """
    This method will create a home page request.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns home page
    """
    return render(request, 'home/home.html')