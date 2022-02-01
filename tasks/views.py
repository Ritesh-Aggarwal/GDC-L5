# Add your Views Here
from django.http import HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task


def index(request):
    existing_tasks = Task.objects.filter(deleted=False,completed=False)
    return render(request, "index.html", {"tasks": existing_tasks})


def completed_task_view(request):
    completed_tasks = Task.objects.filter(deleted=False,completed=True)
    return render(request, "completed.html", {"tasks": completed_tasks})


def all_tasks_view(request):
    existing_tasks = Task.objects.filter(deleted=False,completed=False)
    completed_tasks = Task.objects.filter(deleted=False,completed=True)
    return render(
        request,
        "all.html",
        {"tasks": {"completed": completed_tasks, "existing": existing_tasks}},
    )


def add_task_view(request):
    task = Task(title=request.GET.get("task"))
    task.save()
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, index):
    # origin = request.headers.get("Referer").split("/")[-2]
    task = Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks/")
    # return HttpResponseRedirect(f"/{origin}/")


def complete_task_view(request, index):
    task = Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks/")
