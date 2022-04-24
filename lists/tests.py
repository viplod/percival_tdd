from django.test import TestCase


class HomePageTest(TestCase):
    '''Тест домашней страницы.'''

    def test_home_page_returns_correct_html(self):
        '''Тест: url '/' преобразуется в представление домашней страницы'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
