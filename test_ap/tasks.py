import time
from celery import shared_task


@shared_task()
def wait_clicking():
    time.sleep(20)
    print('Подождали 20 секунд, полет нормальный!')

