# coding:utf-8
from __future__ import absolute_import  # 拒绝隐式引入，因为celery.py和celery包冲突
from celery import Celery


app = Celery('proj', include=['proj.tasks'])
'''app是Celery类的实例，创建的时候添加proj.tasks这个模块，也就是包含了pro/tasks这个文件'''
app.config_from_object('proj.celeryconfig')
if __name__ == '__main__':
    app.start()

