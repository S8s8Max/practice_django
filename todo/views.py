from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        "title":"TODO/Index",
        "msg":"This is a todo application.",
        "goto":"next",
    }
    return render(request, "todo/index.html", params)

def next(request):
    params = {
        "title":"TODO/Next",
        "msg":"This is another page.",
        "goto":"index",
    }
    return render(request, "todo/index.html", params)


