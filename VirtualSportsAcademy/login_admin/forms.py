from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    print "asdad"
    print "chnanges"
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")
