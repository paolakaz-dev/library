from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

from management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),


    path('sign_up/', views.SignUp, name='sign_up'),
    path('change_password/', views.ChangePassword, name='change_password'),

    path('books/', views.BookListView, name='books'),
    path('book/<int:pk>', views.BookDetailView, name='book-detail'),
    path('book/create/', views.BookCreate, name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate, name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete, name='book_delete'),

    path('magazines/', views.MagazineListView, name='magazines'),
    path('magazine/<int:pk>', views.MagazineDetailView, name='magazine-detail'),
    path('magazine/create/', views.MagazineCreate, name='magazine_create'),
    path('magazine/<int:pk>/update/', views.MagazineUpdate, name='magazine_update'),
    path('magazine/<int:pk>/delete/', views.MagazineDelete, name='magazine_delete'),

    path('student/<int:pk>/delete/', views.StudentDelete, name='student_delete'),
    path('student/create/', views.StudentCreate, name='student_create'),
    path('student<int:pk>/update/', views.StudentUpdate, name='student_update'),
    path('student/<int:pk>', views.StudentDetail, name='student_detail'),
    path('student/', views.StudentList, name='student_list'),
    path('student/book_list', views.student_BookListView, name='book_student'),
    path('student/magazine_list', views.student_MagazineListView, name='magazine_student'),
    path('book/<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),
    path('magazine/<int:pk>/request_issue_mag/', views.student_request_issue_mag, name='request_issue_mag'),

    path('bookborrower/', views.BookBorrowerView, name='bookborrower'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('request_password_reset/', views.request_password_reset, name='request_password_reset'),
    path('return/<int:pk>', views.ret, name='ret'),


]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
