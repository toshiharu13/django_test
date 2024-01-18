from django.shortcuts import render
import time


def index(request):
    return render(request, 'index.html')


def get_click(request):
    time.sleep(10)
    text = 'Кнопка нажата'
    context = {
        'text': text,
    }
    return render(request, 'index.html', context=context)
