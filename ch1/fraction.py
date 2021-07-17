class Fraction:
    def __init__(self, top: int, bottom: int):
        assert type(top) == int and type(
            bottom) == int, 'num and den can only be integers.'
        assert bottom != 0, 'cannot divide by 0.'
        common = self.gcd(top, bottom)
        if bottom < 0:
            bottom = -bottom
            top = -top
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        if self.num % self.den == 0:
            return f'{self.num // self.den}'
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    # def __iadd__(self, other):
    #     self.num = self.num * other.den + other.num * self.den
    #     self.den = self.den * other.den

    #     return self

    def __radd__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def show(self):
        print(f'{self.num}/{self.den}')

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n


my_fraction = Fraction(-5, 10)
f2 = Fraction(4, 10)
f3 = Fraction(1, 5)
my_fraction.show()
f2.show()
my_fraction += f2
print(my_fraction)
