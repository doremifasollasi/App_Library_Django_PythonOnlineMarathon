from book.models import Book
from .models import Order
from django.forms import ModelForm, TextInput
from django import forms


class CustomBookName(forms.ModelMultipleChoiceField):
    def label_from_instance(self, book):
        return f'{book.name}'


class OrderForm(ModelForm):
    #books = CustomBookName(
     #   queryset=Book.objects.all()
    #)

    class Meta:
        model = Order
        fields = ['user', 'book', 'plated_end_at']


        #fields = '__all__' #if we wont all fields
        #widgets ={ 'book': forms.Select(attrs={'style': 'width:20px'}) }


