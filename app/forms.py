from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Applicant



class ResumeForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'phone','qualifications']




class FileUploadForm(forms.Form):
    data_file = forms.FileField(label='Upload new data file')




