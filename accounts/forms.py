from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    # email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateAccountForm(object):
    """docstring for CreateAccountForm"""
    # def __init__(self, arg):
    #     super(CreateAccountForm, self).__init__()
    #     self.arg = arg
    #     