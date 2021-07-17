from stack import Stack


def divide_by_2(decimal_num):
    s = Stack()
    bin_str = ''

    while decimal_num > 0:
        s.push(decimal_num % 2)
        decimal_num //= 2

    while not s.is_empty():
        bin_str += str(s.pop())

    return bin_str


def base_converter(decimal_num, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    converted_str = ''

    while decimal_num > 0:
        s.push(decimal_num % base)
        decimal_num //= base
    while not s.is_empty():
        converted_str += ddigits[s.pop()]

    return converted_str


print(divide_by_2(3))
print(divide_by_2(42))
print(base_converter(25, 2))
print(base_converter(256, 16))
print(base_converter(25, 8))
