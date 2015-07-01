from django.test import TestCase
from django.core.urlresolvers import reverse


class SitemapTests(TestCase):

    def test_about_page(self):
        '''
        Checks if about is rendered at <host>/about
        '''
        response = self.client.get(reverse('sitemap:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, 'about')

    def test_faq_page(self):
        '''
        Checks if FAQ is rendered at <host>/faq
        '''
        response = self.client.get(reverse('sitemap:faq'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, 'faq')

    def test_tos_page(self):
        '''
        Checks if ToS is rendered at <host>/tos
        '''
        response = self.client.get(reverse('sitemap:tos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, 'tos')