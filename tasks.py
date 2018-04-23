from celery import Celery
import time   # This is to discover various task ralated features


app = Celery('tasks', broker='amqp://localhost//', backend='db+mysql://root:lmtech123@localhost:3306/celery_database')
# result_backend = 'db+scheme://user:password@host:port/dbname'


@app.task
def add(x, y):
    time.sleep(10)   # This delay is to see the task status as pending
    return x + y
# defined a single task, called add, returning the sum of two numbers.

