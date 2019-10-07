from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import Type
from webapp.forms import TypeForm
from django.views.generic import ListView


class TypeList(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'type/type.html'



class TypeIndex(TemplateView):
    template_name = 'type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = Type.objects.all()
        return context



class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TypeForm()
            return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
            types=form.cleaned_data['type'],

            )
            return redirect('type_add')
        else:
            return render(request,'type/type_create.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        if request.method == 'GET':
            form = TypeForm(data={
                'type': type
            })
        return render(request, 'type/type_update.html', context={'form': form, 'type': type})

    def post(self, request, pk, *args, **kwargs):
        form = TypeForm(data=request.POST)
        type = get_object_or_404(Type, pk=pk)
        return render(request, 'type/type_update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        type = get_object_or_404(Type, pk=pk)
        if request.method == 'GET':
            return render(request, 'type/type_delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('type_read')





