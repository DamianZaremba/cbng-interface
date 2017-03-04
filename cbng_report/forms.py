from django import forms


class ReportForm(forms.Form):
    id = forms.IntegerField(label='Report ID')
    comment = forms.CharField(label='Comment', required=False,
                              help_text='Comments are completely optional. You do not have to justify your edit.')


class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', required=True,
                              help_text='Leaving a comment is completely optional.')
