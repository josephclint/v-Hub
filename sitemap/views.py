from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'sitemap/index.html')

def about(request):
    return HttpResponse('About Page')

def faq(request):
    return HttpResponse('FAQ Page')

def tos(request):
    return HttpResponse('TOS Page')