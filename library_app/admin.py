from django.contrib import admin

# MODELS WHICH WILL BE DISPLAYED IN THE ADMIN PANEL
from .models import *
admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Student)
admin.site.register(BookBorrower)


