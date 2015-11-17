from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    print email
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")
