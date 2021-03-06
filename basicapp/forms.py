from django import forms
from basicapp.models import Projects

class NewUser(forms.ModelForm):
    class Meta():
        model = Projects
        fields = ' __all__'























'''from django import forms
from django.forms.widgets import HiddenInput
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure the email is correct')
        

    
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0 :
            raise forms.ValidationError('GOTCHA BOT')
        return botcatcher
'''