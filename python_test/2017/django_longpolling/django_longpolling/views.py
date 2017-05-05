# coding:utf-8
import Queue

from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

from django_longpolling.helper import Reader



def index(request):
    return render_to_response('index.html')


def get_photo(request):
    if request.method == 'GET':
        r = Reader()
        words = r.get_words()
        print words
        response_data = {'msg': words}
        return render_to_response(json.dumps(response_data))
    # error_data = {"msg": "error"}
    # return HttpResponse(json.dumps(error_data), content_type="application/json")