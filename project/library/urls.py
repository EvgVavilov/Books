from django.urls import path, re_path
from django.conf.urls.static import static
from django.views.static import serve

from library import views
from project import settings

urlpatterns = [
    path('', views.BooksList.as_view(), name="home"),
    path('book/<slug:book_slug>/', views.BookDetail.as_view(), name='book'),
    path('authors/', views.AuthorsList.as_view(), name="authors"),
    path('author/<slug:author_slug>/', views.AuthorDetail.as_view(), name='author'),
    path('add/', views.AddForm.as_view(), name="add"),
    path('add/author/', views.add_author, name="add_author"),
    path('add/book/', views.add_book, name="add_book"),
    path('add/not_valid/', views.not_valid, name="not_valid"),
    path("about/", views.about, name="about"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]

