from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

from .models import *
from .forms import *

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

# HOME PAGE
def index(request):
    return render(
        request,
        'index.html',
    )


# ALL BOOKS IN LIBRARY
def BookListView(request):
    book_list = Book.objects.all()
    # GET ALL OBJECTS
    return render(request, 'library/book_list.html', locals())

# STUDENT=USER / CREATING AN 1:1 RELATION
@login_required
def student_BookListView(request):
    student=Student.objects.get(name=request.User) #problem IntegrityError at /student/create/UNIQUE constraint failed: auth_user.username
    bor= BookBorrower.objects.filter(student=student)
    book_list=[]
    for b in bor:
        # GET ALL OBJECTS
        book_list.append(b.book)


    return render(request, 'library/book_list.html', locals())

# SPECIFIC BOOK
# primary_key TO INDENTIFY BOOK
#get_object_404 ERROR WHEN BOOK DOES NOT EXIST
#locals RETURN DICTIONARY OF LOCAL VAR
def BookDetailView(request, pk):
    book = get_object_or_404(Book, id=pk)
    try:
        stu = Student.objects.get(name=request.user)
    except:
        pass
    return render(request, 'library/book_detail.html', locals())

@login_required
def BookBorrowerView(request):
    #if not request.user.is_superuser:
        #return redirect('index')
     
        bookborrowers = BookBorrower.objects.all()
        context = {
            'bookborrowers': bookborrowers
        }
        return render(request, 'library/borrower.html', locals())



@login_required
def BookCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'library/form.html', locals())


@login_required
def BookUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(index)
    return render(request, 'library/form.html', locals())


@login_required
def BookDelete(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    return redirect('index')
    
# CONDITION FOR TAKING THE BOOK
# INSERT LIMITATION
# Check out a book for up to 30 days
# up to ten books at any given time.

# check out up to three magazines, up to 7 days
@login_required
def student_request_issue(request, pk):
    obj = Book.objects.get(id=pk)
    stu=Student.objects.get(name=request.user)
    s = get_object_or_404(Student, name=str(request.user))
    if s.total_books_due <= 10:
        message = "book has been isuued, You can collect book from library"
        a = BookBorrower()
        a.student = s
        a.book = obj
        a.issue_date = datetime.datetime.now()
        obj.available_copies = obj.available_copies-1
        obj.save()
        stu.total_books_due=stu.total_books_due+1
        stu.save()
        a.save()
    else:
        message = "you have exceeded limit."
    return render(request, 'library/result.html', locals())

# CHECK OUT MAGAZINE
# check out up to three magazines, up to 7 days
@login_required
def student_request_issue_mag(request, pk):
    obj = Magazine.objects.get(id=pk)
    stu=Student.objects.get(name=request.user)
    s = get_object_or_404(Student, name=str(request.user))
    if s.total_magazines_due <= 3:
        message = "magazine has been isuued, You can collect magazine from library"
        a = BookBorrower()
        a.student = s
        a.magazine = obj
        a.issue_date = datetime.datetime.now()
        obj.available_copies = obj.available_copies-1
        obj.save()
        stu.total_magazines_due=stu.total_magazines_due+1
        stu.save()
        a.save()
    else:
        message = "you have exceeded limit."
    return render(request, 'library/result.html', locals())

# ALL MAGAZINES IN LIBRARY
def MagazineListView(request):
    magazine_list = Magazine.objects.all()
    return render(request, 'library/magazine_list.html', locals())

@login_required
def student_MagazineListView(request):
    student=Student.objects.get(name=request.user)
    bor=BookBorrower.objects.filter(student=student)
    magazine_list=[]
    for b in bor:
        magazine_list.append(b.book)
    return render(request, 'library/magazine_list.html', locals())

def MagazineDetailView(request, pk):
    magazine = get_object_or_404(Magazine, id=pk)
    try:
        stu = Student.objects.get(name=request.user)
    except:
        pass
    return render(request, 'library/magazine_detail.html', locals())



@login_required
def MagazineCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = MagazineForm()
    if request.method == 'POST':
        form = MagazineForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'library/magazine_form.html', locals())


@login_required
def MagazineUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Magazine.objects.get(id=pk)
    form = MagazineForm(instance=obj)
    if request.method == 'POST':
        form = MagazineForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(index)
    return render(request, 'library/magazine_form.html', locals())


@login_required
def MagazineDelete(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = get_object_or_404(Magazine, pk=pk)
    obj.delete()
    return redirect('index')





@login_required
def StudentCreate(request):
    if not request.user.is_superuser:
        return redirect('index')
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            s=form.cleaned_data['name']
            form.save()
            u=User.objects.get(username=s)
            s=Student.objects.get(name=s)
            u.email=s.email
            u.save()
            return redirect(index)
    return render(request, 'library/form.html', locals())


@login_required
def StudentUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(index)
    return render(request, 'library/form.html', locals())


@login_required
def StudentDelete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('index')

@login_required
def StudentList(request):
    students = Student.objects.all()
    return render(request, 'library/student_list.html', locals())

@login_required
def StudentDetail(request, pk):
    student = get_object_or_404(Student, id=pk)
    books=BookBorrower.objects.filter(student=student)
    return render(request, 'library/student_detail.html', locals())


def SignUp(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/sign_up.html', context)


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

# RETURN FUNCTION FOR BOOKS
@login_required
def ret(request, pk):
    if not request.user.is_superuser:
        return redirect('index')
    obj = BookBorrower.objects.get(id=pk)
    book_pk=obj.book.id
    student_pk=obj.student.id
    student = Student.objects.get(id=student_pk)
    student.total_books_due=student.total_books_due-1
    student.save()

    book=Book.objects.get(id=book_pk)
    book.available_copies=book.available_copies+1
    book.save()
    obj.delete()
    return redirect('index')

@login_required
def delete_account(request):
    if request.method == "POST":
        if request.POST['confirm_deletion'] == "DELETE":
            user = authenticate(
                request, username=request.user.username, password=request.POST['password'])
            if user:
                print(f"Deleting user {user}")
                user.delete()
                return HttpResponseRedirect(reverse('index'))
            else:
                print("fail delete")

    return render(request, 'registration/delete_account.html')

def password_reset(request):
    if request.method == "POST":
        post_user = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        token = request.POST['token']

        if password == confirm_password:
            try:
                prr = PasswordResetRequest.objects.get(token=token)
                prr.save()
            except:
                print("Invalid password reset attempt.")
                return render(request, 'registration/password_reset.html')

            user = prr.user
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'registration/password_reset.html')


def request_password_reset(request):
    if request.method == "POST":
        post_user = request.POST['username']
        user = None

        if post_user:
            try:
                user = User.objects.get(username=post_user)
            except:
                print(f"Invalid password request: {post_user}")
        else:
            post_user = request.POST['email']
            try:
                user = User.objects.get(email=post_user)
            except:
                print(f"Invalid password request: {post_user}")
        if user:
            prr = PasswordResetRequest()
            prr.user = user
            prr.save()
            print(prr)
            return HttpResponseRedirect(reverse('password_reset'))
    return render(request, 'registration/request_password_reset.html')




