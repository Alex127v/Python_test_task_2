"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""


def get_views_count(n: int) -> str:
    last_two_number = n % 100
    last_number = n % 10
    if any([11 <= last_two_number <= 14,
            5 <= last_number <= 9,
            last_number == 0]):
        return f'{n} просмотров'
    if 2 <= last_number <= 4:
        return f'{n} просмотра'
    return f'{n} просмотр'


if __name__ == '__main__':
    assert get_views_count(0) == '0 просмотров'
    assert get_views_count(1) == '1 просмотр'
    assert get_views_count(2) == '2 просмотра'
    assert get_views_count(4) == '4 просмотра'
    assert get_views_count(5) == '5 просмотров'
    assert get_views_count(9) == '9 просмотров'
    assert get_views_count(11) == '11 просмотров'
    assert get_views_count(14) == '14 просмотров'
    assert get_views_count(15) == '15 просмотров'
    assert get_views_count(20) == '20 просмотров'
    assert get_views_count(21) == '21 просмотр'
    assert get_views_count(22) == '22 просмотра'
    assert get_views_count(107) == '107 просмотров'
    print('All tests passed')