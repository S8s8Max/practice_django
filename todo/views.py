from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm

def index(request):
    params = {
        "title":"TODO",
        "message":"your data :",
        "form":TodoForm(),
    }
    if (request.method == "POST"):
        params["message"] = "Name : " + request.POST["name"] + \
            "<br>mail : " + request.POST["mail"] + \
            "<br>age : " + request.POST["age"]
        params["form"] = TodoForm(request.POST)
    return render(request, "todo/index.html", params)


