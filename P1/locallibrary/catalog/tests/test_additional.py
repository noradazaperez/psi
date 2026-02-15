from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission  # Required to grant the
# permission needed to set a book as returned.

from catalog.models import Author

User = get_user_model()


class AuthorDeleteViewTest(TestCase):
    """Test case for the AuthorCreate view (Created as Challenge)."""

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='test_user', password='some_password')

        permAuthor = Permission.objects.get(
            codename="delete_author"
        )

        test_user.user_permissions.add(permAuthor)
        test_user.save()

        test_user1 = User.objects.create_user(username='testuser1',
                                              password='1X<ISRUkw+tuK')
        test_user1.save()

        self.test_author = Author.objects.create(first_name='Dominique',
                                                 last_name='Rousseau')

        self.test_author.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('author-delete',
                                           kwargs={'pk': self.test_author.pk}))
        # Manually check redirect (Can't use assertRedirect,
        # because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_logged_in_with_permission(self):
        self.client.login(username='test_user',
                          password='some_password')
        response = self.client.get(reverse('author-delete',
                                           kwargs={'pk': self.test_author.pk}))

        # Check that it lets us see the view
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username='test_user', password='some_password')

        response = self.client.get(reverse('author-delete',
                                           kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_confirm_delete.html')
