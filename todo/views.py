from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all()
    params = {
        "title" : "todo",
        "data" : data,
    }
    return render(request, "todo/index.html", params)

# create model
def create(request):
    if (request.method == "POST"):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/todo")
    params = {
        "title": "Todo",
        "form": FriendForm(),
    }
    return render(request, "todo/create.html", params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == "POST"):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/todo")
    params = {
        "title": "Todo",
        "id": num,
        "form": FriendForm(instance=obj),
    }
    return render(request, "todo/edit.html", params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == "POST"):
        friend.delete()
        return redirect(to="/todo")
    params = {
        "title": "Todo",
        "id": num,
        "obj": friend,
    }
    return render(request, "todo/delete.html", params)
