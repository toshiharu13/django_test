from django.shortcuts import render
import time
from . tasks import wait_clicking


def index(request):
    return render(request, 'index.html')


def get_click(request):
    text = 'Кнопка нажата'
    context = {'text': text}
    wait_clicking.delay()
    return render(request, 'index.html', context=context)
