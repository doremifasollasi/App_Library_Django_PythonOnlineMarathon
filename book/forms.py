from .models import Book
from .models import Author
from django.forms import ModelForm, TextInput, Textarea

# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "description", "count", "authors"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input name"
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Input description"
            }),
            "count": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input count"
            }),
            
        }
