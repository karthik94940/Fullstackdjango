from django import forms
from user_registration.models import User


class UserForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        fields = "__all__"