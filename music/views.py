from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('hello world')

def detail(request):
    return HttpResponse('Details for Album id: ' + str('album_id'))