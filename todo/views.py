from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def home_page(request: HttpRequest) -> HttpResponse:
    queryset = Task.objects.all().prefetch_related("tags")

    per_page = request.GET.get('per_page')
    if not per_page or 0 > int(per_page) > 20:
        per_page = request.session.get("per_page", 5)

    page = request.GET.get('page')

    paginator = Paginator(queryset, per_page)


    try:
        objects = paginator.page(page)

    except PageNotAnInteger:
        objects = paginator.page(1)

    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    is_paginated = False

    if paginator.num_pages > 1:
        is_paginated = True

    context = {
        "task_list": objects,
        "page_obj": objects,
        "paginator": paginator,
        "is_paginated": is_paginated,
    }

    return render(request, "todo/home_page.html", context=context)


def task_undo(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = False
    task.save()
    return redirect("todo:home-page")


def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = True
    task.save()
    return redirect("todo:home-page")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home-page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home-page")

class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
