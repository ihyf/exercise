from __future__ import absolute_import
from celery import Celery
app = Celery('myTasks', include=['myTasks.tasks'])
app.config_from_object('myTasks.config')