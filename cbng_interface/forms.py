from django import forms


class PreferencesForm(forms.Form):
    next_on_review = forms.BooleanField(label='Auto redirect on review',
                                        required=False)
