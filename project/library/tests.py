from django.test import TestCase
from django.urls import reverse

from library.models import Book, Author


class BooksApiTestCase(TestCase):
    def setUp(self):
        test_author = Author.objects.create(id=1, name='test_author', about_author='test_text', slug='test_author')
        test_book1 = Book.objects.create(id=1, name='test_book1', about_book='test_text', slug='test_book1', )
        test_book2 = Book.objects.create(id=2, name='test_book2', about_book='test_text', slug='test_book2', )
        test_book1.author.add(test_author)
        test_book2.author.add(test_author)

    def test_get_response(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertEqual(self.client.get(reverse('book', kwargs={"book_slug": 'test_book1'})).status_code, 200)
        self.assertEqual(self.client.get(reverse('book', kwargs={"book_slug": 'not_exist_book'})).status_code, 404)
        self.assertEqual(self.client.get(reverse('authors')).status_code, 200)
        self.assertEqual(self.client.get(reverse('author', kwargs={"author_slug": 'test_author'})).status_code, 200)
        self.assertEqual(self.client.get(reverse('author',
                                                 kwargs={"author_slug": 'not_exist_author'})).status_code, 404)
        self.assertEqual(self.client.get(reverse('about')).status_code, 200)
        self.assertEqual(self.client.get(reverse('add')).status_code, 302)
        self.assertEqual(self.client.get(reverse('not_valid')).status_code, 200)
        self.assertEqual(self.client.get(reverse('register')).status_code, 200)
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
        self.assertEqual(self.client.get(reverse('logout')).status_code, 302)
        self.assertEqual(self.client.get('/not_exist_path/').status_code, 404)

    def test_book_list(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.context_data['object_list'].get(id=1).slug, 'test_book1')
        self.assertEqual(response.context_data['object_list'].get(id=2).slug, 'test_book2')

    def test_author_list(self):
        url = reverse('authors')
        response = self.client.get(url)

        self.assertEqual(response.context_data['object_list'].get(id=1).slug, 'test_author')
        self.assertEqual(Book.objects.get(slug='test_book1').author.first(),
                         response.context_data['object_list'].get(id=1))

    def test_register_login(self):
        # register
        self.client.post(reverse('register'), data={'username': 'test_user',
                                                    'password1': 'kaikaikai',
                                                    'password2': 'kaikaikai'})
        response = self.client.get(reverse('home'))
        self.assertEqual(response.wsgi_request.user.username, 'test_user')
        # logout
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.wsgi_request.user.username, '')
        # login
        response = self.client.post(reverse('login'), data={'username': 'test_user',
                                                            'password': 'kaikaikai'})
        self.assertEqual(response.wsgi_request.user.username, 'test_user')
