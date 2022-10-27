from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator

from webapp.models import Task, Project


def max_length_validator(string):
    if len(string) > 30:
        raise ValidationError('Maximum length of string is 20 symbols')
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=30, message=''):
        message = 'Maximum value %(limit_value)s you entered %(show_value)s values'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200,
                            label='Title',
                            validators=(
                                MinLengthValidator(limit_value=2, message=''),
                                CustomLengthValidator(limit_value=30),
                                )
                            )

    class Meta:
        model = Task
        fields = ('title', 'description', 'types', 'statuses')


class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label='Title',
                            validators=(
                                MinLengthValidator(limit_value=2, message=''),
                                CustomLengthValidator(limit_value=30),
                                )
                            )

    class Meta:
        model = Project
        fields = ('title', 'description', 'task')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')
