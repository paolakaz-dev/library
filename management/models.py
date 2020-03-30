from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.db.models.signals import post_save
from django import forms
import datetime


# GANGRE BOOK
class Genre(models.Model):
    name = models.CharField(max_length=200)
##  __str__ METHOD IS TO OVERRIDE THE DEFAULT STRING
    def __str__(self):
        return self.name


## LANGUAGE
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# BOOK 
# RELATION WITH GANGRE AND LANGUAGE BOOK
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic=models.ImageField(blank=True, null=True, upload_to='book_image')

# RETURN URL FOR EN OBJECT
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
#MAGAZINE
# RELATION WITH LANGUAGE
class Magazine(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the magazine")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic=models.ImageField(blank=True, null=True, upload_to='magazine_image')

# RETURN URL FOR EN OBJECT
    def get_absolute_url(self):
        return reverse('magazine-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

# USER CREATION
def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'],password="dummypass")
# STUDENT CREATION
class Student(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10)
    branch = models.CharField(max_length=3)
    contact_no = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    pic=models.ImageField(blank=True, upload_to='profile_image')
    def __str__(self):
        return str(self.roll_no)

# SAVE AFTER CREATION
post_save.connect(create_user, sender=Student)

# BORROWER CREATION
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, help_text= "You can check book only up to 30 days")
    issue_date = models.DateTimeField( null=True,blank=True)
    return_date = models.DateTimeField( null=True,blank=True)
    def __str__(self):
        return self.student.name+" borrowed "+self.book.title 

#magazine = models.ForeignKey('Magazine', on_delete=models.CASCADE, null=True, help_text= "You can check out up to 3 magazines" )
#+" and "+self.magazine.title
#Customers can check out a book for up to 30 days,
# and they can check out up to ten books at any given time.
#  They can also check out up to three magazines, up to 7 days. 
# When someone reaches the limit or have outstanding checkouts, 
# they can’t check out more books or magazines before the check in 
# some other book or magazine first and don’t have any outstanding checkouts. 
# Nobody should ever have more than ten books, and three magazines checked out.




