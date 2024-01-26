from django.core.exceptions import ValidationError
from django.shortcuts import render
import time
from . tasks import wait_clicking
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from django.utils import timezone
from contextlib import suppress


def index(request):
    return render(request, 'index.html')


def get_click(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute='15',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    print(schedule)
    with suppress(ValidationError):
        taska, _ = PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name='Repeat order_2',
            task='repeat_order_make',
        )
    print(taska)
    text = 'Кнопка нажата'
    context = {'text': text}
    wait_clicking.delay()
    return render(request, 'index.html', context=context)
