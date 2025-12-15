"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число бинарным поиском

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1  # Нижняя граница
    high = 100  # Верхняя граница
    
    while low <= high:
        count += 1
        mid = (low + high) // 2  # Предполагаемое число
        
        if mid == number:
            return count  # Угадали
        elif mid < number:
            low = mid + 1  # Искомое число больше
        else:
            high = mid - 1  # Искомое число меньше
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(42)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")


if __name__ == "__main__":
    # RUN
    score_game(random_predict)