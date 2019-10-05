from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.forms import TaskForm
from webapp.models import Task
from webapp.models import Status
from webapp.forms import StatusForm
from webapp.models import Type
from webapp.forms import TypeForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.all()
        return render(request, 'index.html', context={
            'task': task
        })

class TaskView(View):
    def get (self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task.html', context={
            'task': task
        })

class TaskCreateView(View):
    def get (self,request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, 'create.html', context={'form': form})

    def post (self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
            summary=form.cleaned_data['summary'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            type=form.cleaned_data['type'],
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class TaskUpdateView(View):
    def get (self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            form = TaskForm(data={
                'summary': task.summary,
                'created_at': task.created_at,
                'description': task.description,
                'type': task.type,
                'status': task.status
            })
            return render(request, 'update.html', context={'form': form, 'task': task})

    def post (self, request, pk, *args, **kwargs):
            form = TaskForm(data=request.POST)
            task = get_object_or_404(Task, pk=pk)
            if form.is_valid():
                task.summary = form.cleaned_data['summary']
                task.description = form.cleaned_data['description']
                task.type = form.cleaned_data['type']
                task.status = form.cleaned_data['status']
                task.save()
                return redirect('task_view', pk=task.pk)
            else:
                return render(request, 'update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            return render(request, 'delete.html', context={'task': task})

    def post (self,request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')


class StatusList(View):
    def get(self, request, *args, **kwargs):
        status = Status.objects.all()
        return render(request, 'status_read.html', context={
            'status': status
        })



class StatusCreateView(View):
    def get (self,request, *args, **kwargs):
        if request.method == 'GET':
            form = StatusForm()
            return render(request, 'status_create.html', context={'form': form})

    def post (self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
            statuses=form.cleaned_data['status'],

            )
            return redirect('status_add')
        else:
            return render(request, 'status_create.html', context={'form': form})



class StatusUpdateView(View):
    def get (self, request, pk, *args, **kwargs):
            status = get_object_or_404(Status, pk=pk)
            if request.method == 'GET':
                form = StatusForm(data={
                    'status': status
                })
            return render(request, 'status_update.html', context={'form': form, 'status': status})

    def post (self, request, pk, *args, **kwargs):
            form = StatusForm(data=request.POST)
            status = get_object_or_404(Status, pk=pk)
            return render(request, 'status_update.html', context={'form': form, 'status': status})



class StatusDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        if request.method == 'GET':
            return render(request, 'status_delete.html', context={'status': status})

    def post (self,request,  *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('status_read')




class TypeList(View):
    def get(self, request, *args, **kwargs):
        type = Type.objects.all()
        return render(request, 'type_read.html', context={
            'type': type
        })


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TypeForm()
            return render(request, 'type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
            types=form.cleaned_data['type'],

            )
            return redirect('type_add')
        else:
            return render(request, 'type_create.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        if request.method == 'GET':
            form = TypeForm(data={
                'type': type
            })
        return render(request, 'type_update.html', context={'form': form, 'type': type})

    def post(self, request, pk, *args, **kwargs):
        form = TypeForm(data=request.POST)
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        if request.method == 'GET':
            return render(request, 'type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('type_read')





