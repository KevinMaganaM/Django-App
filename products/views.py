from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('The products will be display here')

def new(request):
    return HttpResponse('new products')