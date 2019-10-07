from django.views.generic import TemplateView
# from webapp.models import Task, Type, Status


class ListView(TemplateView):
    context_key = 'object'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()
        return context

    def get_objects(self):
        return self.model.objects.all()