from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm
from django.views.generic import TemplateView

class TodoView(TemplateView):

    def __init__(self):
        self.params = {
            "title": "TODO",
            "form": TodoForm(),
            "result": None,
        }

    def get(self, request):
        return render(request, "todo/index.html", self.params)

    def post(self, request):
        ch = request.POST.getlist("choice")
        self.params["result"] = "You selected: " + str(ch) + "."
        self.params["form"] = TodoForm(request.POST)
        return render(request, "todo/index.html", self.params)


