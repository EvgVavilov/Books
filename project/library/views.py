from typing import Any

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from library import forms
from library.models import Author, Book

menu = [
    {"title": "Книги", "url_name": "home"},
    {"title": "Авторы", "url_name": "authors"},
    {"title": "Добавить", "url_name": "add"},
    {"title": "О сайте", "url_name": "about"},
]


class BooksList(generic.ListView):
    model = Book
    template_name = "library/books_list.html"
    context_object_name = "books"

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = "Книги"
        ctx["menu"] = menu
        return ctx


class BookDetail(generic.DetailView):
    model = Book
    template_name = "library/book_detail.html"
    slug_url_kwarg = "book_slug"
    context_object_name = "book"

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = self.object.name
        ctx["menu"] = menu
        return ctx


class AuthorsList(generic.ListView):
    model = Author
    template_name = "library/authors_list.html"
    context_object_name = "authors"

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = "Авторы"
        ctx["menu"] = menu
        return ctx


class AuthorDetail(generic.DetailView):
    model = Author
    template_name = "library/author_detail.html"
    slug_url_kwarg = "author_slug"
    context_object_name = "author"

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = self.object.name
        ctx["menu"] = menu
        return ctx


class AddForm(LoginRequiredMixin, generic.View):
    template_name = "library/add.html"
    login_url = reverse_lazy('login')

    def get(self, request: HttpRequest) -> HttpResponse:
        ctx = {"title": "Добавить",
               "menu": menu,
               'author_form': forms.CreateAuthorForm,
               'book_form': forms.CreateBookForm}
        return render(request, "library/add.html", ctx)


def add_author(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateAuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('not_valid')


def add_book(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('not_valid')


def not_valid(request: HttpRequest) -> HttpResponse:
    context = {'message': '''Проверьте коректность введённых вами данных! Убедитесь что заполнили все обязательные поля!
     Слаг должен состоять из букв, цифр, латинских букв, нижнего подчёркивания и дефиса!
     Слаг должен быть уникальным!''',
               "menu": menu}
    return render(request, template_name="library/form_not_valid.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    context = {"title": "О сайте",
               "menu": menu}
    return render(request, template_name="library/about.html", context=context)


class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = "library/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = "Регистрация"
        ctx["menu"] = menu
        return ctx

    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "library/login.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> HttpResponse:
        ctx = super().get_context_data()
        ctx["title"] = "Войти"
        ctx["menu"] = menu
        return ctx

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy("home")


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("login")
