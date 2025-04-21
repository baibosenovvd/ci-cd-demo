import logging
from file2 import second_function

logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')

def first_function(data):
    if data is None:
        raise ValueError("Пустые данные")
    if data < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return data * 2

def log_error(message):
    logging.error(f"Ошибка при обработке данных: {message}")

def main_process(data):
    try:
        result = first_function(data)  # вызывается первая функция
        return second_function(result)  # если успешно — вызывается вторая функция
    except Exception as e:
        log_error(str(e))
        return None
