from django import forms
from django.forms import widgets
from webapp.models import Status,Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=40, required=True, label='Текст')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label="Status")
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label="Type")



class StatusForm(forms.Form):
    status = forms.CharField(max_length=50,label=None)


class TypeForm(forms.Form):
    type = forms.CharField(max_length=50,label=None)