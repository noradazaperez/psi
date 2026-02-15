from django.test import TestCase
from django.urls import reverse

from catalog.models import Author
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.models import Permission # Required to grant the permission needed to set a book as returned.

class AuthorDeleteViewTest(TestCase):
    """Test case for the AuthorCreate view (Created as Challenge)."""

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='test_user', password='some_password')

        permAddAuthor = Permission.objects.get(
            codename="add_author"
        )

        test_user.user_permissions.add(permAddAuthor)
        test_user.save()

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        test_author = Author.objects.create(
                first_name=f'Dominique',
                last_name=f'Surname',
            )
        
        test_author.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_logged_in_with_permission(self):
        login = self.client.login(username='test_user', password='some_password')
        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))

        # Check that it lets us see the view
        self.assertEqual(response.status_code, 200)
    
    def test_uses_correct_template(self):
        self.client.login(username='test_user', password='some_password')

        response = self.client.get(reverse('author-delete', kwargs={'pk': self.test_author.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_confirm_delete.html')
'''

    def test_form_date_of_death_initially_set_to_expected_date(self):
        login = self.client.login(username='test_user', password='some_password')
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)

        inital_date = datetime.datetime(2023, 11, 11)
        self.assertEqual(response.context['form'].initial['date_of_death'], inital_date)
        
    def test_redirects_to_detail_view_on_success(self):
        login = self.client.login(username='test_user', password='some_password')
        valid_date_in_future = datetime.date.today() + datetime.timedelta(weeks=2)
        response = self.client.post(reverse('author-create'), {'first_name':'Big', 'last_name':'Bob'})

        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/catalog/author/'))
'''