import os
import time
from datetime import datetime

from celery import Celery


celery = Celery("tasks", broker="redis://127.0.0.1:63790")
celery.conf.CELERY_RESULT_BACKEND = 'redis://127.0.0.1:63790'


@celery.task
def add(x, y):
    return int(x) + int(y)


@celery.task
def sleep(seconds):
    time.sleep(float(seconds))
    return seconds


@celery.task
def echo(msg, timestamp=False):
    return "%s: %s" % (datetime.now(), msg) if timestamp else msg


@celery.task
def error(msg):
    raise Exception(msg)


if __name__ == "__main__":
    celery.start()
