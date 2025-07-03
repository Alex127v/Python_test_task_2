from get_views_count import get_views_count


def test_get_views():
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
    assert get_views_count(25) == '25 просмотров'
