from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.views.generic import TemplateView
from webapp.forms import TaskForm
from webapp.models import Task
from django.views.generic import ListView,CreateView



class IndexView(ListView):
    context_object_name = 'task'
    model = Task
    template_name = 'task/index.html'
    ordering = ['created_at']
    paginate_by = 2
    paginate_orphans = 1


class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context
#
#
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})

#     def get (self,request, *args, **kwargs):
#         if request.method == 'GET':
#             form = TaskForm()
#             return render(request, 'task/create.html', context={'form': form})
#
#     def post (self, request, *args, **kwargs):
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task = Task.objects.create(
#             summary=form.cleaned_data['summary'],
#             description=form.cleaned_data['description'],
#             status=form.cleaned_data['status'],
#             type=form.cleaned_data['type'],
#             )
#             return redirect('task_view', pk=task.pk)
#         else:
#             return render(request, 'task/create.html', context={'form': form})
#

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
            return render(request, 'task/update.html', context={'form': form, 'task': task})

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
                return render(request, 'task/update.html', context={'form': form, 'task': task})


class TaskDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            return render(request, 'task/delete.html', context={'task': task})

    def post (self,request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')

