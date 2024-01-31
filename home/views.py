
# Create your views here.
# home/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data=[
        {
            "name": "John",
            "age": 30
        },
        {
            "name": "Mary",
            "age": 25
        },
        {
            "name": "Peter",
            "age": 20
        },
        {
            "name": "Lisa",
            "age": 25
        },
    ]
    return render(request, 'pages/index.html', context={'data': data})


def about(request):
    return render(request, 'pages/about.html')