from django.http import HttpResponse
from django.shortcuts import render


def calculate():
    x=1
    y=20
    return y
# Create your views here.
def say_hello(request):
    # return render(request, 'hello.html', {'name':'Josh'})
    x = calculate()
    return render(request, 'hello.html')

