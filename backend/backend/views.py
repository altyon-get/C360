from django.shortcuts import render
from django.http import JsonResponse

def hello(request):
    data = {'message': 'Hello, from Django backend!'}
    return JsonResponse(data)