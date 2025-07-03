from get_growth import get_pct_growth

def test_get_growth():
    assert get_pct_growth([100, 150, 300, 400]) == [None, '50%', '100%', '33%']
    assert get_pct_growth([30, 20, 25, 50]) == [None, '-33%', '25%', '100%']
    print('All tests pass')