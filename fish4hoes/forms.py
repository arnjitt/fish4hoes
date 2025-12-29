from django import forms
from django.forms import modelformset_factory
from .models import Friend

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ["name", "energy"]

FriendEnergyFormSet = modelformset_factory(
  Friend,
  fields=["energy"],
  extra=0
)