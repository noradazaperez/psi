from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission  # Required to grant the
# permission needed to set a book as returned.

import datetime

from catalog.models import Author, Genre, Book, BookInstance
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.models import Permission


class AuthorDeleteViewTest(TestCase):
    """Test case for the Author delete view and permissions."""

    def setUp(self):
        # Create a user with delete permission
        test_user = User.objects.create_user(username='test_user', password='some_password')
        permAuthor = Permission.objects.get(codename="delete_author")
        test_user.user_permissions.add(permAuthor)
        test_user.save()

        self.test_author = Author.objects.create(first_name='Dominique', last_name='Rousseau')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_logged_in_with_permission(self):
        self.client.login(username='test_user', password='some_password')
        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username='test_user', password='some_password')
        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_confirm_delete.html')


class ModelsTests(TestCase):
    """Test case for Genre, Book, BookInstance and Author models."""

    def test_genre_str_and_url(self):
        g = Genre.objects.create(name='Sci-Fi')
        self.assertEqual(str(g), 'Sci-Fi')

    def test_book_str_url_and_display_genre(self):
        a = Author.objects.create(first_name='Isaac', last_name='Asimov')
        b = Book.objects.create(title='I Robot', author=a, summary='x', isbn='1234567890123')
        g1 = Genre.objects.create(name='Science Fiction')
        b.genre.add(g1)
        self.assertEqual(str(b), 'I Robot')
        self.assertEqual(b.get_absolute_url(), reverse('book-detail', args=[str(b.id)]))
        self.assertIn('Science Fiction', b.display_genre())

    def test_bookinstance_str(self):
        a = Author.objects.create(first_name='Stephen', last_name='King')
        b = Book.objects.create(title='The Shining', author=a, summary='x', isbn='9780345806789')
        bi = BookInstance.objects.create(book=b, imprint='First', due_back=datetime.date.today())
        self.assertIn('The Shining', str(bi))

    def test_author_display_genre_from_books(self):
        a = Author.objects.create(first_name='Test', last_name='Author')
        g = Genre.objects.create(name='Drama')
        b = Book.objects.create(title='Drama Book', author=a, summary='x', isbn='1111111111111')
        b.genre.add(g)

class ViewsTests(TestCase):
    """Test case for views"""

    @classmethod
    def setUpTestData(cls):
        # Create test authors
        cls.author1 = Author.objects.create(first_name='Isaac', last_name='Asimov')
        cls.author2 = Author.objects.create(first_name='Stephen', last_name='King')

        # Create genres
        cls.genre_scifi = Genre.objects.create(name='Science Fiction')
        cls.genre_horror = Genre.objects.create(name='Horror')

        # Create books
        cls.book1 = Book.objects.create(
            title='I Robot',
            author=cls.author1,
            summary='Robot stories',
            isbn='1234567890123'
        )
        cls.book1.genre.add(cls.genre_scifi)

        cls.book2 = Book.objects.create(
            title='The Shining',
            author=cls.author2,
            summary='Horror novel',
            isbn='9780345806789'
        )
        cls.book2.genre.add(cls.genre_horror)

        cls.book3 = Book.objects.create(
            title='Foundation',
            author=cls.author1,
            summary='Foundation series',
            isbn='0553293356'
        )
        cls.book3.genre.add(cls.genre_scifi)

    def test_index_view_status(self):
        """Test that index view returns 200 and uses correct template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_context(self):
        """Test that index view provides all expected context variables."""
        response = self.client.get(reverse('index'))
        self.assertIn('num_books', response.context)
        self.assertIn('num_instances', response.context)
        self.assertIn('num_instances_available', response.context)
        self.assertIn('num_authors', response.context)
        self.assertIn('num_genres', response.context)
        self.assertIn('num_books_word', response.context)

    def test_book_list_view(self):
        """Test BookListView shows books and pagination works."""
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_list.html')
        self.assertTrue('is_paginated' in response.context)

    def test_book_detail_view(self):
        """Test BookDetailView shows correct book."""
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['book'], self.book1)
        self.assertTemplateUsed(response, 'catalog/book_detail.html')

    def test_author_list_view(self):
        """Test AuthorListView shows authors and pagination works."""
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')
        self.assertTrue('is_paginated' in response.context)

    def test_author_detail_view(self):
        """Test AuthorDetailView shows correct author."""
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.author1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['author'], self.author1)
        self.assertTemplateUsed(response, 'catalog/author_detail.html')

    def test_author_create_view_requires_permission(self):
        """Test AuthorCreate requires add_author permission."""
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

        # Login and try without permission
        user = User.objects.create_user(username='noauth', password='pass')
        self.client.login(username='noauth', password='pass')
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_author_create_view_with_permission(self):
        """Test AuthorCreate view with proper permission."""
        user = User.objects.create_user(username='author_creator', password='pass')
        perm = Permission.objects.get(codename='add_author')
        user.user_permissions.add(perm)
        self.client.login(username='author_creator', password='pass')

        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_form.html')

    def test_author_create_post_redirects(self):
        """Test AuthorCreate POST with valid data redirects."""
        user = User.objects.create_user(username='author_creator', password='pass')
        perm = Permission.objects.get(codename='add_author')
        user.user_permissions.add(perm)
        self.client.login(username='author_creator', password='pass')

        response = self.client.post(reverse('author-create'), {
            'first_name': 'New',
            'last_name': 'Author',
            'date_of_birth': '1980-01-01',
            'date_of_death': ''
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

    def test_author_update_view(self):
        """Test AuthorUpdate view."""
        user = User.objects.create_user(username='author_updater', password='pass')
        perm = Permission.objects.get(codename='change_author')
        user.user_permissions.add(perm)
        self.client.login(username='author_updater', password='pass')

        response = self.client.get(reverse('author-update', kwargs={'pk': self.author1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_form.html')

    def test_author_delete_delete_view(self):
        """Test AuthorDelete with POST deletes author."""
        user = User.objects.create_user(username='author_deleter', password='pass')
        perm = Permission.objects.get(codename='delete_author')
        user.user_permissions.add(perm)
        self.client.login(username='author_deleter', password='pass')

        author_pk = self.author1.pk
        response = self.client.post(reverse('author-delete', kwargs={'pk': author_pk}))
        self.assertEqual(response.status_code, 302)

    def test_book_create_view(self):
        """Test BookCreate view requires permission."""
        user = User.objects.create_user(username='book_creator', password='pass')
        perm = Permission.objects.get(codename='add_book')
        user.user_permissions.add(perm)
        self.client.login(username='book_creator', password='pass')

        response = self.client.get(reverse('book-create'))
        self.assertEqual(response.status_code, 200)

    def test_book_update_view(self):
        """Test BookUpdate view requires permission."""
        user = User.objects.create_user(username='book_updater', password='pass')
        perm = Permission.objects.get(codename='change_book')
        user.user_permissions.add(perm)
        self.client.login(username='book_updater', password='pass')

        response = self.client.get(reverse('book-update', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, 200)

    def test_book_delete_view(self):
        """Test BookDelete view requires permission."""
        user = User.objects.create_user(username='book_deleter', password='pass')
        perm = Permission.objects.get(codename='delete_book')
        user.user_permissions.add(perm)
        self.client.login(username='book_deleter', password='pass')

        book_pk = self.book1.pk
        response = self.client.post(reverse('book-delete', kwargs={'pk': book_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=book_pk).exists())

    def test_loaned_books_by_user_list_view(self):
        """Test LoanedBooksByUserListView requires login."""
        response = self.client.get(reverse('my-borrowed'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Login and check view
        user = User.objects.create_user(username='borrower', password='pass')
        self.client.login(username='borrower', password='pass')
        response = self.client.get(reverse('my-borrowed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')

    def test_loaned_books_all_list_view(self):
        """Test LoanedBooksAllListView requires permission."""
        response = self.client.get(reverse('all-borrowed'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Login with permission
        user = User.objects.create_user(username='librarian', password='pass')
        perm = Permission.objects.get(codename='can_mark_returned')
        user.user_permissions.add(perm)
        self.client.login(username='librarian', password='pass')
        response = self.client.get(reverse('all-borrowed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed.html')

    def test_renew_book_librarian_get(self):
        """Test renew_book_librarian GET shows form."""
        # Create a book instance
        book_instance = BookInstance.objects.create(
            book=self.book1, imprint='Test', status='o'
        )
        user = User.objects.create_user(username='lib', password='pass')
        perm = Permission.objects.get(codename='can_mark_returned')
        user.user_permissions.add(perm)
        self.client.login(username='lib', password='pass')

        response = self.client.get(reverse('renew-book-librarian', kwargs={'pk': book_instance.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_renew_librarian.html')
        self.assertIn('form', response.context)

    def test_renew_book_librarian_post_valid(self):
        """Test renew_book_librarian POST with valid form."""
        book_instance = BookInstance.objects.create(
            book=self.book1, imprint='Test', status='o'
        )
        user = User.objects.create_user(username='lib', password='pass')
        perm = Permission.objects.get(codename='can_mark_returned')
        user.user_permissions.add(perm)
        self.client.login(username='lib', password='pass')

        future_date = (datetime.date.today() + datetime.timedelta(weeks=2)).isoformat()
        response = self.client.post(reverse('renew-book-librarian', kwargs={'pk': book_instance.pk}), {
            'renewal_date': future_date
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success