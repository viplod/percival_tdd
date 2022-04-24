from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    '''Тест домашней страницы.'''

    def test_uses_home_template(self):
        '''Тест: url '/' преобразуется в представление домашней страницы'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        '''Тест: может сохранить post-запрос'''
        self.client.post('/', data={
            'item_text': 'Новый элемент списка'
        })
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'Новый элемент списка')

    def test_redirects_after_POST(self):
        '''Тест переадресует после post-запроса'''
        response = self.client.post('/', data={
            'item_text': 'Новый элемент списка'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        '''Тест: сохраняет элементы, только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        '''Тест: отображаются все элементы списка'''
        Item.objects.create(text='Элемент 1')
        Item.objects.create(text='Элемент 2')

        response = self.client.get('/')

        self.assertIn('Элемент 1', response.content.decode())
        self.assertIn('Элемент 2', response.content.decode())


class ItemModelTest(TestCase):
    '''Тест модели элемента списка.'''

    def test_saving_and_retrieving_items(self):
        '''Тест сохранения и получения элементов списка.'''
        first_item = Item()
        first_item.text = 'Первый элемент'
        first_item.save()

        second_item = Item()
        second_item.text = 'Второй элемент'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Первый элемент')
        self.assertEqual(second_saved_item.text, 'Второй элемент')
