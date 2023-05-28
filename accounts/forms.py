from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        # widgets = {
        #     'email': forms.EmailInput(attrs = {'class': 'form-field', 'placeholder':'Enter Email', 'type':'email'})
        # }

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'password do not match')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-field'
            self.fields[field].widget.attrs['placeholder'] = f'Enter {field}'
