import os
from datetime import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        path = 'main.log'
        # start = datetime.now()
        start = datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
        result = old_function(*args, **kwargs)
        with open(path, 'a+', encoding='utf-8') as f:
            f.write(f'Дата вызова функции: {start}. '
                    f'Имя функции: {old_function.__name__}. '
                    f'Аргументы: {args}, {kwargs}, '
                    f'Значение функции: {result}\n')
        return result
    return new_function

def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=2, b=3)

    with open(path, encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()