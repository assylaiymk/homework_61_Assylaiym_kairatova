from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label_suffix='Login')
    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)
