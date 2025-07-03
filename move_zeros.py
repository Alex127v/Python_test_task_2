"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции
    (функция ничего не возвращает)
"""


def move_zeros(lst: list[float]) -> list:
    num_list = [i for i in lst if i != 0]
    zero_list = [n for n in lst if n == 0]
    return num_list + zero_list


def move_zeros_2(lst: list[float]):
    count_zero = lst.count(0)
    for _ in range(count_zero):
        lst.remove(0)
    lst.extend([0] * count_zero)


if __name__ == '__main__':
    assert move_zeros([7, 0, 0, 2, 3, 0, 1]) == [7, 2, 3, 1, 0, 0, 0]
    print('Tests_1 passed')
    test_list = [7, 0, 0, 2, 3, 0, 1]
    move_zeros_2(test_list)
    assert test_list == [7, 2, 3, 1, 0, 0, 0]
    print('Tests_2 passed')