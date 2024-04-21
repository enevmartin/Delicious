# recipes/tests.py
from django.http import Http404
from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe


class RecipesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description'
        )

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)

    def test_all_recipe_list_view(self):
        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)

    # Add more tests for other views as needed...

    def test_custom_404_handling(self):
        with self.assertRaises(Http404):
            response = self.client.get('/nonexistent-url/')

    def test_custom_500_handling(self):
        response = self.client.get(reverse('nonexistent-view'))
        self.assertEqual(response.status_code, 500)
