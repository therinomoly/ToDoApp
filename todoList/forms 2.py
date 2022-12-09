from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):

    class Meta:
        model = Todo
        fields = ['task_name']
        labels={
            'task_name': 'Task name'
        }
        widgets={
            'task_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add a new task'
            })
        }