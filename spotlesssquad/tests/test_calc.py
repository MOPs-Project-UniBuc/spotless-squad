from spotlesssquad.calc.common import calc_sum


def test_add():
    assert 1 + 1 == 2


def test_calc_sum():
    assert calc_sum(1, 2) == 3
