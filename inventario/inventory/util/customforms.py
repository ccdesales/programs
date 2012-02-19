'''
Created on Dec 13, 2011

@author: desales
'''

from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from inv.models import Item, Inventory, InventoryEntry

from django.forms import ( 
    ModelForm,
    Select, 
    CharField,
    Textarea,
    RadioSelect,
    SelectMultiple, 
    ModelMultipleChoiceField, 
    CheckboxSelectMultiple
)

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ('name', 'items', 'ttype')
        #fields = ('name', 'ttype')
        widgets = {
            'ttype': RadioSelect(),
        }
        
