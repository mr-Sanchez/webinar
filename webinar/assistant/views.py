from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hi!')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
