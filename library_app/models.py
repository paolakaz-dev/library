from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.db.models.signals import post_save
from django import forms
import datetime


# BOOK 
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic=models.ImageField(blank=True, null=True, upload_to='book_image')

# RETURN URL FOR EN OBJECT
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
#MAGAZINE
class Magazine(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
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
    nr = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10, unique=True)
    contact_nr = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    pic=models.ImageField(blank=True, upload_to='profile_image')
    def __str__(self):
        return str(self.nr)

# SAVE AFTER CREATION
post_save.connect(create_user, sender=Student)

# BOOK BORROWER CREATION
class BookBorrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, help_text= "You can check book only up to 30 days")
    issue_date = models.DateTimeField( null=True,blank=True)
    return_date = models.DateTimeField( null=True,blank=True)
    def __str__(self):
        return self.student.name+" borrowed "+ self.book.title 

#magazine = models.ForeignKey('Magazine', on_delete=models.CASCADE, null=True, help_text= "You can check out up to 3 magazines" )
#+" and "+self.magazine.title
#Customers can check out a book for up to 30 days,
# and they can check out up to ten books at any given time.
#  They can also check out up to three magazines, up to 7 days. 
# When someone reaches the limit or have outstanding checkouts, 
# they can’t check out more books or magazines before the check in 
# some other book or magazine first and don’t have any outstanding checkouts. 
# Nobody should ever have more than ten books, and three magazines checked out.




