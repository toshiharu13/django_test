import time
from celery import shared_task


@shared_task()
def wait_clicking():
    time.sleep(20)
    print('Подождали 20 секунд, полет нормальный!')


@shared_task(name="repeat_order_make")
def repeat_order_make():
    print('Нужно повторно оформлять заказ каждые несколько минут')