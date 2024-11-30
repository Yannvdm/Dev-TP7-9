import pytest
from Fract import Fraction

def test_construct():
    f1 = Fraction(1,1)
    assert f1._num == 1
    assert f1._den == 1

    f2 = Fraction(1,-2)
    assert f2._num == -1
    assert f2._den == 2

    f3 = Fraction(5)
    assert f3._num == 5
    assert f3._den == 1

def test_construct_0_den():
    with pytest.raises(ValueError, match="denominator cannot be zero"):
        Fraction(2,0)

def test_construct_no_int():
    with pytest.raises(TypeError, match="num and den must be integers"):
        Fraction('hello', 1)

def test_construct_default():
    f4 = Fraction()
    assert f4._num == 0
    assert f4._den == 1

def test_is_zero():
    assert Fraction(0,1).is_zero() is True
    assert Fraction(4,1).is_zero() is False

def test_as_mixed_number():
    assert Fraction(4, 1).as_mixed_number() == "4"
    assert Fraction(-4, 4).as_mixed_number() == "-1"
    assert Fraction(6, 4).as_mixed_number() == "1 1/2"

def test_str():
    assert str(Fraction(1,2)) == "1/2"
    assert str(Fraction(2,1)) == "2"
    assert str(Fraction(2, 4)) == "1/2"

def test_add():
    f1 = Fraction(1,2)
    other = Fraction(1,3)
    assert f1 + other == Fraction(5,6)

def test_add_not_fraction():
    with pytest.raises(TypeError, match="Other is not a Fraction"):
        Fraction(1, 2) + 1

def test_truediv():
    f1 = Fraction(2,4)
    other = Fraction(1,3)
    assert f1 / other == Fraction(6,4)


def test_truediv_not_fraction():
    with pytest.raises(TypeError, match="Other is not a Fraction"):
        Fraction(1, 2) / 1

def test_eq():
    f1 = Fraction(1,2)
    f2 = Fraction(1,3)
    f3 = Fraction(1,2)
    assert (f1 == f2) == False
    assert (f1 == f3) == True

def test_eq_no_fract():
    with pytest.raises(TypeError, match="Other is not a Fraction"):
        result = Fraction(1, 2) == 1

def test_is_integer():
    f1 = Fraction(2,1)
    f2 = Fraction(4, 8)
    f3 = Fraction(8, 4)
    assert f1.is_integer() is True
    assert f2.is_integer() is False
    assert f3.is_integer() is True

def test_is_proper():
    f1 = Fraction(2, 1)
    f2 = Fraction(4, 8)
    f3 = Fraction(8, 4)
    assert f1.is_proper() is False
    assert f2.is_proper() is True
    assert f3.is_proper() is False

def test_is_unit():
    f1 = Fraction(2, 1)
    f2 = Fraction(4, 8)
    f3 = Fraction(1, 2)
    assert f1.is_unit() is False
    assert f2.is_unit() is True
    assert f3.is_unit() is True
#Bonus

def test_lt():
    f1 = Fraction(2, 1)
    f2 = Fraction(4, 8)
    assert (f1 < f2) == False
    f3 = Fraction(2, 1)
    f4 = Fraction(9, 4)
    assert (f3 < f4) == True

def test_gt():
    f1 = Fraction(2, 1)
    f2 = Fraction(4, 8)
    assert (f1 > f2) == True
    f3 = Fraction(2, 1)
    f4 = Fraction(9, 4)
    assert (f3 > f4) == False

