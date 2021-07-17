class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


def rev_string(my_str):
    s = Stack()
    rev_str = ''
    for char in my_str:
        s.push(char)
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


if __name__ == '__main__':
    print(rev_string('bao hsiao'))
