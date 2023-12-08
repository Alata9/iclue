from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, DateInput, DateField, ChoiceField

from articles.models import Items, Questions, Subsections


class SubsectionAdd(ModelForm):
    class Meta:
        model = Subsections
        fields = ('name', 'section')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].empty_label = ''
        self.fields['section'].required = True
        self.fields['name'].label = 'Item'
        self.fields['name'].required = True


class ItemAdd(ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'subsection')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subsection'].empty_label = ''
        self.fields['subsection'].required = True
        self.fields['name'].label = 'Item'
        self.fields['name'].required = True


class QuestionsAdd(ModelForm):
    class Meta:
        model = Questions
        fields = ('item', 'name', 'answer',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = ''
        self.fields['item'].required = True
        self.fields['name'].label = 'Questions'
        self.fields['name'].required = True
        self.fields['answer'].label = 'Inswer'
        self.fields['answer'].required = True
