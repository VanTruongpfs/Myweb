from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>hello</h1>")
    response.write("this is app home")
    return response