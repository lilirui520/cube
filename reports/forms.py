#! -*- encoding: utf-8 -*-

from django import forms

class CreateReportForm(forms.Form):
    start_date = forms.DateField(label="起始日期(required)")
    end_date = forms.DateField(label="结束日期(required)")
    cur_done = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label="上周完成工作 (required)", max_length=400)
    next_goal = forms.CharField(widget=forms.Textarea(attrs={'rows':4}),label="本周任务计划 (required)", max_length=400)
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':4}), label="工作中的意见和建议(not required)", max_length=400)
    # email = forms.EmailField(required=False)
    # password = forms.CharField(widget=forms.PasswordInput())
