from django import forms
from .models import Conference , Submission

class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','description','start_date','end_date']
        labels = {
            'name': "Titre de la conférence",
            'theme': "Thème de la conférence",
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"entrer un titre à la conférence",}),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'}),
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model=Submission
        fields=['title','abstract','paper','status','payed','user','conference']
        labels = {
            'title': "Titre de la soumission",
            'abstract': "Résumé de la soumission",
        }
        widgets={
            'title':forms.TextInput(attrs={'placeholder':"entrer un titre à la soumission",}),
            'paper':forms.FileInput(),

        }