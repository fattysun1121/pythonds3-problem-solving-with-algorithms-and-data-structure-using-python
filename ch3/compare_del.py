import timeit
import pandas as pd
import matplotlib.pyplot as plt


def del_li(size):
    del li[0]
    del li[size // 2]
    del li[-1]


def del_di(size):
    del di[0]
    del di[size // 2]
    del di[size - 1]


def build_collection(n, t):
    if t == 'l':
        global li
        li = list(range(n))
    global di
    di = {i: str(i) for i in range(n)}


data: dict = {'Size': [], 'Time': []}
t1 = timeit.Timer(
    'del_li(size)',
    'from __main__ import del_li, size, build_collection; build_collection(size, "l")')
for size in range(1000, 100001, 5000):
    times = t1.repeat(25, 1)
    data['Size'].append(size)
    data['Time'].append(min(times))
df = pd.DataFrame(data=data)
ax = df.plot.scatter(x='Size', y='Time', color='blue')

data = {'Size': [], 'Time': []}
t2 = timeit.Timer(
    'del_di(size)',
    'from __main__ import del_di, size, build_collection; build_collection(size, "d")')
for size in range(1000, 100001, 5000):
    times = t2.repeat(25, 1)
    data['Size'].append(size)
    data['Time'].append(min(times))
df = pd.DataFrame(data=data)
df.plot.scatter(x='Size', y='Time', ax=ax, c='red')

plt.show()
