from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View


def HelloworldView(request):
    return HttpResponse("helloworld")