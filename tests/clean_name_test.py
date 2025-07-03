from clean_name import clean_name

def test_clean_name():
    assert clean_name('Иsвtrан Ив^%ан Ива?но)вич') == 'Иван Иван Иванович'
    assert clean_name('А%%ле?ксей Ал"е+к-са;ндро)вич Б9ато№в') == 'Алексей Александрович Батов'
    print('All test pass')