from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ('category','name','description','price','image')
    
    
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter category","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter name","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter description","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':"Enter price","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':"Enter image","class":'w-full py-4 px-6 rounded-xl'}), required=True)
    