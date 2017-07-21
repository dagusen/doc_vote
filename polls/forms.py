from django import forms
from .models import Question, Choice
from django.forms.formsets import BaseFormSet


class QuestionModelForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class ChoiceFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(ChoiceFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
