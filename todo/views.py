from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm
from django.views.generic import TemplateView

class TodoView(TemplateView):

    def __init__(self):
        self.params = {
            "title": "TODO",
            "message": "your data : ",
            "form": TodoForm(),
        }

    def get(self, request):
        return render(request, "todo/index.html", self.params)

    def post(self, request):
        msg = "You are <b>" + request.POST["name"] + \
            "(" + request.POST["age"] + ") <b>. <br>Your mail is <b>" + \
            request.POST["mail"] + "<br>."
        self.params["message"] = msg
        self.params["form"] = TodoForm(request.POST)
        return render(request, "todo/index.html", self.params)


