from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()
    high_priority_tasks = tasks.filter(priority='High').count()

    all_completed = total_tasks > 0 and completed_tasks == total_tasks

    

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'high_priority_tasks': high_priority_tasks,
        'all_completed': all_completed,
    }

    return render(request, 'tasks/task_list.html', context)


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})



def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/delete_task.html', {'task': task})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)

    task.completed = not task.completed
    task.save()

    return redirect('task_list')