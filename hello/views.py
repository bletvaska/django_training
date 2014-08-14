from django.shortcuts import render, HttpResponse


# Create your views here.
def ahoj(request):
    return HttpResponse("hello world!")


# def greetings(request, name):
    # return render(request, 'base.html', {'name': 'User' if name is None else name})


def greetings(request, name=None):
    if name is None:
        name = 'User'
    return render(request, 'base.html', {'name': name})
