import timeit
import pandas as pd
import matplotlib.pyplot as plt


def build_collection(n, t):
    if t == 'l':
        return list(range(n))
    return {i: str(i) for i in range(n)}


def test_index(n):
    li[0]
    li[n // 2]
    li[n - 1]


def test_item(n):
    di[0]
    di[n // 2]
    di[n - 1]
    di[0] = ''
    di[n // 2] = ''
    di[n - 1] = ''


data = {'Size': [], 'Speed': []}

t1 = timeit.Timer('test_index(size)', 'from __main__ import test_index, size, li')
for size in range(1000, 100001, 5000):
    li = build_collection(size, 'l')
    times = t1.repeat(100, 25)
    data['Size'].append(size)
    data['Speed'].append(min(times))
df = pd.DataFrame(data=data)
df.plot.scatter(x='Size', y='Speed').plot


data = {'Size': [], 'Speed': []}
t2 = timeit.Timer('test_item(size)', 'from __main__ import test_item, size, di')
for size in range(1000, 100001, 5000):
    di = build_collection(size, 'd')
    times = t2.repeat(100, 25)
    data['Size'].append(size)
    data['Speed'].append(min(times))
df = pd.DataFrame(data=data)
df.plot.scatter(x='Size', y='Speed').plot()
plt.show()
