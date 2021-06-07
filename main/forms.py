from .models import User
from django.forms import ModelForm, TextInput, EmailInput, RadioSelect

class RegForm(ModelForm):
  class Meta:
    model = User
    fields = ["name", "nickname", "gender", "email", "password"]