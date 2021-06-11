from django.db.models import fields
from django.forms import ModelForm
from .models import * 

class AuthorForm(ModelForm):
    class Meta: 
        model = Authors
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        