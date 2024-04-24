from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .tasks import get_price

def my_view(request):
    # Call the Celery task
    print('Task queued!')
    get_price.delay()
    return HttpResponse("Task queued!")

