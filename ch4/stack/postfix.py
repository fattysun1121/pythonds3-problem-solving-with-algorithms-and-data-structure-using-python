from stack import Stack
from string import ascii_uppercase


def infix_to_postfix(infix_expr: str):
    op_stack = Stack()
    postfix_list = []
    token_list: list = infix_expr.split(' ')
    prec = {
        '(': -1,
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '**': 2,
    }

    for token in token_list:
        if token in ascii_uppercase or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()
        elif token in '*/+-**':
            while (not op_stack.is_empty()) \
                    and prec[token] <= prec[op_stack.peek()]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split(' ')

    for token in token_list:
        if token in '0123456789':
            operand_stack.push(token)
        elif token in '*/+-':
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = f'{operand1} {token} {operand2}'
            operand_stack.push(eval(result))
        else:
            raise KeyError(f'Unavailable Input: {token}')
    return float(operand_stack.pop())


print(infix_to_postfix('A * B + C * D'))
print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))
print(infix_to_postfix('5 * 3 ** ( 4 - 2 )'))
print(postfix_eval('7 8 + 3 2 + /'))
