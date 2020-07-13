from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        "title":"TODO/Index",
        "msg":"What is your name?",
    }
    return render(request, "todo/index.html", params)

def form(request):
    msg = request.POST["msg"]
    params = {
        "title":"TODO/Next",
        "msg":"Hello, " + msg + ".",
    }
    return render(request, "todo/index.html", params)


