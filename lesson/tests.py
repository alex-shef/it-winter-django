from django.test import TestCase, Client
import ddt
from lesson import models
# Create your tests here.


@ddt.ddt
class MaterialTestCase(TestCase):

    def setUp(self):
        super(MaterialTestCase, self).__init__()
        self.client = Client()
        self.user = models.User(first_name='maxim')
        self.user.save()

    def test_material_created_return_200(self):
        response = self.client.post('/create/',
                                    {"title":"test_title",
                                     "body": 'mybody',
                                     "status": 'private'})
        self.assertEqual(response.status_code, 200)

    def test_material_created_one(self):
        response = self.client.post('/create/',
                                    {"title": "test_title",
                                     "body": 'mybody',
                                     "status": 'private'})
        mat = models.Material.objects.get()
        self.assertEqual(mat.title, "test_title")

    @ddt.data("slug1", "slug3", "slug3")
    def test_slug_created(self, expected_slug):
        """test slug={} created correctly"""
        response = self.client.post('/create/',
                                    {"title": expected_slug,
                                     "body": 'mybody',
                                     "status": 'private'})
        mat = models.Material.objects.get()
        self.assertEqual(mat.slug, expected_slug)

    @ddt.data(
        ("slu g1", "slu-g1"),
        ("s lug 3", "s-lug-3"),
        ("slug 3", "slug-3"),
    )
    @ddt.unpack
    def test_slug_created_correctly(self, title, expected_slug):
        """test slug={} created correctly"""
        response = self.client.post('/create/',
                                    {"title": title,
                                     "body": 'mybody',
                                     "status": 'private'})
        mat = models.Material.objects.get()
        self.assertEqual(mat.slug, expected_slug)