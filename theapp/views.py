from django.shortcuts import render

# Create your views here.

def test(requests):
    return render(requests, 'test.html')

def test2(requests):
    return render(requests, 'test2.html')