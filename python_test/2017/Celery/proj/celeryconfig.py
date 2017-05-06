# coding:utf-8
# 使用RabbitMQ作为消息代理
BROKER_URL = 'amqp://192.168.0.1:5672//'
# 把任务结果存在redis里
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'
# 读取任务结果一般性能不高，所以使用了json
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间
CELERY_TASK_RESULT_EXPIRES = 60*60*24
# 指定接收的内容范围
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

