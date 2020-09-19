from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Task
from .forms import FriendForm, TaskForm
from .forms import CheckForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max
from django.core.paginator import Paginator

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request, num=1):
    data = Friend.objects.all() # Friend DBから取り出すデータを指定。
    page = Paginator(data, 3) # ページネータ。表示させる数を設定。
    params = {
        "title" : "todo",
        "message" : "",
        "data" : page.get_page(num),
    }
    print(data)
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

def find(request):
    if (request.method == "POST"):
        msg = "search result : "
        form = FindForm(request.POST)
        find = request.POST["find"]
        lst = find.split()
        data = Friend.objects.all()[int(lst[0]):int(lst[1])]
        msg = "Result : " + str(data.count())
    else:
        msg = "search words ..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title": "Todo",
        "message": msg,
        "form": form,
        "data": data,
    }
    return render(request, "todo/find.html", params)

def check(request):
    params = {
        "title" : "Todo",
        "message" : "check validation",
        "form" : FriendForm(),
    }
    if (request.method == "POST"):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params["form"] = form
        if (form.is_valid()):
            params["message"] = "OK"
        else:
            params["message"] = "NG"
    return render(request, "todo/check.html", params)

def task(request, page=1):
    if (request.method == "POST"):
        obj = Task()
        form = TaskForm(request.POST, instance=obj)
        form.save()
    data = Task.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        "title": "Task",
        "form": TaskForm(),
        "data": paginator.get_page(page),
    }
    return render(request, "todo/task.html", params)
