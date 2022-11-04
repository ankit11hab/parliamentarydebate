import email
from django import forms
from typing import NewType

from more_itertools import collapse
from .models import teams,adjudicators,crossOpen
from django.contrib.auth import get_user_model



class institutionCreationsForm(forms.ModelForm):
  email=forms.EmailField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  POCname=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  college=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  contactno=forms.CharField(
   widget=forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", 
  )
  teamSlots=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
    model=teams
    fields=['POCname','email','college','contactno','teamSlots','info']

class crossOpenCreationsForm(forms.ModelForm):
  email=forms.EmailField(widget=forms.TextInput(
    attrs={'class':'input_field'}
  ))
  TeamName=forms.CharField(
    widget=forms.TextInput(attrs={'class':'input_field'})
  )
  Country=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  contactno=forms.CharField(widget=forms.TextInput(attrs={
    'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
  Name_of_Poc=forms.CharField(
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
      model=crossOpen
      fields=['TeamName','email','Country','contactno','Name_of_Poc','info']

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
  contactno=forms.CharField(widget=forms.TextInput(attrs={
    'class': 'input_field', 'placeholder': 'Phone Number (e.g. +12125552368) *'}), label="Phone number (e.g. +12125552368)", )
 
  TournamentName=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  Year=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  Format=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  Size=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  POB=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  OutroundSpoken=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  awards=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )
  info=forms.CharField(required = False,
   widget=forms.TextInput(attrs={'class':'input_field'})
  )

  class Meta:
      model=adjudicators
      fields=['name','email','college','contactno','POB','info','OutroundSpoken','awards','Year','Format','Size','TournamentName']

