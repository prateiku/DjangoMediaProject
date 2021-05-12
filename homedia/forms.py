from django import forms

class fileform(forms.Form):
    file_up = forms.FileField(label='Select a file')

class check_box(forms.Form):
    choices = forms.MultipleChoiceField(
        #choices = LIST_OF_VALID_CHOICES, # this is optional
        widget= forms.MultipleChoiceField,
    )