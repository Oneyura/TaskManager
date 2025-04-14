from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "index"
    template_name = "todo_list/index.html"

class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo-list:index")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo-list:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:index")


class TaskCompleteView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.status = True
        task.save()
        return redirect("todo-list:index")


class TaskUndoView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.status = False
        task.save()
        return redirect("todo-list:index")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list:tags.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo-list:tag-list")

class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo-list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo-list:tag-list")
