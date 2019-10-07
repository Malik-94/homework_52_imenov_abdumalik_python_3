from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from django.views.generic import TemplateView
from webapp.forms import TaskForm
from webapp.models import Task
from django.views.generic import ListView,CreateView
from webapp.views.base_views import UpdateView



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


class TaskCreateView(View):
    def get (self,request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, 'task/create.html', context={'form': form})

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
            return render(request, 'task/create.html', context={'form': form})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/update.html'
    context_key = 'task'
    form_class = TaskForm

    def get_redirect_url(self):
        return reverse ('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'GET':
            return render(request, 'task/delete.html', context={'task': task})

    def post (self,request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')

