import email
from django import forms
from typing import NewType

from more_itertools import collapse
from .models import teams,adjudicators,crossOpen
from django.contrib.auth import get_user_model



class institutionCreationsForm(forms.ModelForm):
  email=forms.EmailField(widget=forms.TextInput(
    attrs={'class':'input_field'}
  ))
  POCname=forms.CharField(
    widget=forms.TextInput(attrs={'class':'input_field'})
  )
  college=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  number=forms.CharField(widget=forms.TextInput(attrs={
    'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
  teamslots=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
    model=teams
    fields=['POCname','email','college','number','teamslots','info']

class crossOpenCreationsForm(forms.ModelForm):
  email=forms.EmailField(widget=forms.TextInput(
    attrs={'class':'input_field'}
  ))
  teamname=forms.CharField(
    widget=forms.TextInput(attrs={'class':'input_field'})
  )
  country=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  number=forms.CharField(widget=forms.TextInput(attrs={
    'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
  POCname=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
      model=crossOpen
      fields=['teamname','email','country','number','POCname','info']

class IndependentAdjudicatorCreationsForm(forms.ModelForm):
  email=forms.EmailField(widget=forms.TextInput(
    attrs={'class':'input_field'}
  ))
  name=forms.CharField(
    widget=forms.TextInput(attrs={'class':'input_field'})
  )
  college=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  number=forms.CharField(widget=forms.TextInput(attrs={
    'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
 
  tourname=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  year=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  format=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  size=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  POB=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  outround=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  awards=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
      model=adjudicators
      fields=['name','email','college','number','POB','info','outround','awards','year','format','size','tourname']

