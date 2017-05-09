# coding:utf-8
import Queue
import time
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

from django_longpolling.helper import Reader

r = Reader()


def index(request):
    return render_to_response('index.html')


def get_photo(request):
    if request.method == 'GET':
        while True:
            words = r.get_words()
            response_data = {'msg': words}
            if words:
                response = HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "*"
                return response
