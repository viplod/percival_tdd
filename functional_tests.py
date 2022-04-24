from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя.'''

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome('yandexdriver.exe', options=options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''Тест: можно начать список и получить его позже.'''

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

    # Ей сразу же предлагается ввести элемент списка
    # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
    # вязание рыболовных мушек)
    # Когда она нажимает enter, страница обновляется, и теперь страница
    # содержит "1: Купить павлиньи перья" в качестве элемента списка
    # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
    # Она вводит "Сделать мушку из павлиньих перьев"
    # (Эдит очень методична)
    # Страница снова обновляется, и теперь показывает оба элемента ее списка
    # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
    # сайт сгенерировал для нее уникальный URL-адрес – об этом
    # выводится небольшой текст с объяснениями.
    # Она посещает этот URL-адрес – ее список по-прежнему там.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
