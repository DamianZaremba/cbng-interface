from django import forms


class SignupForm(forms.Form):
    comment = forms.CharField(label='Comment', required=True)
    username = forms.CharField(label='Wikipedia username', required=True, disabled=True)
