from math import gcd


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num an int
              den an int that can't be equal to 0
        POST : doesn't return anything but creates a Fraction instance
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('num and den must be integers')

        if den == 0:
            raise ValueError('denominator cannot be zero')

        self._num = num
        self._den = den

        if den < 0:
            self._num = -self._num
            self._den = -self._den

    def reduce(self):
        """Simplify the fraction by dividing numerator and denominator by their GCD."""
        divisor = gcd(self._num, self._den)
        self._num //= divisor
        self._den //= divisor


    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : returns in text form a representation of the fraction
        """
        self.reduce()

        if self._den == 1:
            return f'{self._num}'
        else : return f'{self._num}/{self._den}'

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : returns in text form a representation of the fraction as a mixed number
        """
        self.reduce()

        if abs(self._num) < abs(self._den):
            return f'{self}'
        else :
            whole = self._num // self._den
            rest = abs(self._num % self._den)
            if rest:
                return f'{whole} {rest}/{self._den}'
            else: return f'{whole}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is an instance of Fraction
         POST : adds two fractions, returns the value and creates a new instance of Fraction

        """

        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        num = self._num * other._den + self._den * other._num
        den = self._den * other._den
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : other is an instance of Fraction
         POST : subtracts two fractions, returns the value and creates a new instance of Fraction

        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        num = self._num * other._den - self._den * other._num
        den = self._den * other._den
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is an instance of Fraction
        POST : multiplies two fractions, returns the value and creates a new instance of Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        num = self._num * other._num
        den = self._den * other._den
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is an instance of Fraction
        POST : divides two fractions, returns the value and creates a new instance of Fraction
        RAISE : ZeroDivisionError if other._num is equal to 0

        """

        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        if other._num == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        num = self._num * other._den
        den = self._den * other._num
        return Fraction(num, den)



    def __pow__(self, power:int):
        """Overloading of the ** operator for fractions

        PRE : -
        POST : returns a new instance of Fraction elevated by power
        """
        num_pow = self._num ** power
        den_pow = self._den ** power
        powered_fraction = Fraction(num_pow, den_pow)
        return powered_fraction.reduce()

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is an instance of Fraction, is not None
        POST : returns True if the two fractions are equal and False if not

        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        return self._num == other._num and self._den == other._den

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : -
        POST : returns float representation of the fraction
        """
        return self._num / self._den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)
    def __lt__(self, other):
        """Compares two Fraction objects and returns True if the fraction is less than the other

        PRE : other is an instance of Fraction, is not None
        POST : returns True if the fraction is less than the other

        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        return self._num * other._den < other._num * self._den

    def __gt__(self, other):
        """Compares two Fraction objects and returns True if the fraction is more than the other

        PRE : other is an instance of Fraction, is not None
        POST : returns True if the fraction is more than the other

        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        return self._num * other._den > other._num * self._den

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : returns True if the fraction is equal to zero
        """
        return self._num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : returns True if the fraction is an integer
        """
        return self._num % self._den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : returns True if the fraction is proper
        """
        return abs(self._num) < abs(self._den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : return True if the fraction is unit in its reduced form
        """
        self.reduce()
        return self._num == 1


    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        PRE : other is an instance of Fraction
        POST : returns True if the fractions are adjacent
        """
        if not isinstance(other, Fraction):
            raise TypeError('Other is not a Fraction')
        return abs(self - other).is_unit()

    def __abs__(self):
        """Overloading of the abs() function for fractions.

        PRE: -
        POST: Returns a new Fraction instance with a positive numerator and denominator.
        """
        return Fraction(abs(self._num), self._den)

