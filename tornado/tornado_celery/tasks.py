#coding:utf-8
import os
from bsddb import db

from celery import Celery

celery=Celery('tasks',broker='amqp://')
celery.conf.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND','amqp')

@celery.tasks(name='task.quey_users')
def query_users(admin_id):
    # 耗时的数据库操作
    return db.query_all_users(admin_id)
