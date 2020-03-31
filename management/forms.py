from django import forms

from .models import *

# CREATING THE FORMS FROM MODELS (FIELDS)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'


class BorrowForm(forms.ModelForm):
    class Meta:
        model = BookBorrower
        exclude = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
