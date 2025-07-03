from move_zeros import move_zeros, move_zeros_2

def test_move_zeros_1():
    assert move_zeros([0, 0, 8, 0, 1, 5]) == [8, 1, 5, 0, 0, 0]
    assert move_zeros([7, 0, 2, 0, 9, 0]) == [7, 2, 9, 0, 0, 0]

def test_move_zeros_2():
    lst_1 = [0, 0, 8, 0, 1, 5]
    move_zeros_2(lst_1)
    assert lst_1 == [8, 1, 5, 0, 0, 0]

    lst_2 = [0, 0, 8, 0, 1, 5]
    move_zeros_2(lst_2)
    assert lst_2 == [8, 1, 5, 0, 0, 0]
