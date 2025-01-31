from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateTimeInput, CheckboxSelectMultiple
from django.utils.timezone import now

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        labels = {
            "content": "Describe your task:"
        }
        widgets = {
            "deadline": DateTimeInput(attrs={
                "type": "datetime-local"
            }),
            "tags": CheckboxSelectMultiple(),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < now():
            raise ValidationError("Deadline cannot be in the past.")
        return deadline
