from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import Status
from webapp.forms import StatusForm


class StatusList(View):
    def get(self, request, *args, **kwargs):
        status = Status.objects.all()
        return render(request, 'status/status_read.html', context={
            'status': status
        })


class StatusCreateView(View):
    def get (self,request, *args, **kwargs):
        if request.method == 'GET':
            form = StatusForm()
            return render(request, 'status/status_create.html', context={'form': form})

    def post (self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
            statuses=form.cleaned_data['status'],

            )
            return redirect('status_add')
        else:
            return render(request, 'status/status_create.html', context={'form': form})



class StatusUpdateView(View):
    def get (self, request, pk, *args, **kwargs):
            status = get_object_or_404(Status, pk=pk)
            if request.method == 'GET':
                form = StatusForm(data={
                    'status': status
                })
            return render(request, 'status/status_update.html', context={'form': form, 'status': status})

    def post (self, request, pk, *args, **kwargs):
            form = StatusForm(data=request.POST)
            status = get_object_or_404(Status, pk=pk)
            return render(request, 'status/status_update.html', context={'form': form, 'status': status})



class StatusDeleteView(View):
    def get (self,request , pk, *args, **kwargs):
        status = get_object_or_404(Status, pk=pk)
        if request.method == 'GET':
            return render(request, 'status/status_delete.html', context={'status': status})

    def post (self,request,  *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('status_read')


