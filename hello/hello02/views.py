from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, 'hello02.html', {'name': 'summer'})


def var01(request):
    lst = ['Python', 'Django', 'Template']
    return render(request, 'variable01.html', {'lst': lst})


def var02(request):
    dct = {'class': 'qclass', 'name': 'summer'}
    return render(request, 'variable02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'numbers': range(1, 10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id': 'qclass', 'name': 'summer'}})


def if02(request):
    return render(request, 'if02.html', {'role': 'manager'})


def href(request):
    return render(request, 'href.html')