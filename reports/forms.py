#! -*- encoding: utf-8 -*-

from django import forms

class CreateReportForm(forms.Form):
    start_date = forms.DateField(label="date began from (required)")
    end_date = forms.DateField(label="date ended to(required)")
    cur_done = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label="what have you done in last week (required)", max_length=400)
    next_goal = forms.CharField(widget=forms.Textarea(attrs={'rows':4}),label="what's your goal this week (required)", max_length=400)
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':4}), label="any comment is acceptable (not required)", max_length=400)
    # email = forms.EmailField(required=False)
    # password = forms.CharField(widget=forms.PasswordInput())
