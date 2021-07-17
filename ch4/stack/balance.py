from stack import Stack


def par_checker(par_str):
    s = Stack()
    for par in par_str:
        if par == '(':
            s.push(par)
        else:
            try:
                s.pop()
            except IndexError:
                return False

    return s.is_empty()


def balance_checker(symbol_str):
    s = Stack()
    for symbol in symbol_str:
        if symbol in '([{':
            s.push(symbol)
        else:
            try:
                if not matches(s.pop(), symbol):
                    return False
            except IndexError:
                return False
    return s.is_empty()


def matches(sym_left, sym_right):
    all_lefts = '([{'
    all_rights = ')]}'
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


print(par_checker(')('))
print(balance_checker('[{()]'))
print(balance_checker('{({([][])}())}'))
