#%%
#1.1 将序列分解为单独的变量

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, b, c, _ = data  #_占位
b, c

#%%
#1.2 解压可迭代对象赋值给多个变量

data = ['ACME', 50, 91.1, (2012, 12, 21)]
a, *b, c = data
b

#%%
#1.3 保留最后 N 个元素 collections.deque

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q
q.appendleft(4)
q
q.pop()
q
q.popleft()

#%%
#1.4 查找最大或最小的 N 个元素 nlargest() nsmallest()

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(11, nums)
heapq.nsmallest(11, nums)
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
#接受一个关键字参数
cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
cheap, expensive

#%%
#1.5 实现一个优先级队列 PriorityQueue()

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
# (priority, item)
a = (1, Item('foo'))
b = (5, Item('bar'))
a < b
# (priority, index, item)
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
a > b, b > c, a == c

#%%
#1.6 字典中的键映射多个值 collections  defaultdict

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d

#%%

d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d

#%%
#1.7 字典排序 collections  OrderedDict

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])

#%%
#1.8 字典的运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
prices_sorted = sorted(zip(prices.values(), prices.keys()))
prices_sorted

#%%

min = heapq.nsmallest(3, prices, key=lambda k: prices[k])
min

#%%
#1.9 查找两字典的相同点

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
# Find keys in common
a.keys() & b.keys()

#%%

# Find keys in a that are not in b
a.keys() - b.keys()

#%%

# Find (key,value) pairs in common
a.items() & b.items()

#%%

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
c

#%%
#1.10 删除序列相同元素并保持顺序

#hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

#%%

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: (d['x'], d['y'])))
list(dedupe(a, key=lambda d: d['x']))
#%%
#1.11 命名切片 slice() 函数创建了一个切片对象

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
items[a]
#%%
items[a] = [10, 11]
items
#%%
del items[a]
items
#%%
#1.12 序列中出现次数最多的元素 collections.Counter类  most_common()

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
top_three
#%%
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
a = Counter(words)
b = Counter(morewords)
c = a + b
c
#%%
d = a - b
d
#%%
#1.13 通过某个关键字排序一个字典列表  operator模块的itemgetter函数

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_fname
#%%
#itemgetter() 函数也支持多个 keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
rows_by_fname
#%%
min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))
#%%
#1.14 排序不支持原生比较的对象

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]

from operator import attrgetter

sorted(users, key=attrgetter('user_id'))
#%%
#1.15 通过某个字段将记录分组 itertools.groupby()

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))  #排序
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):  #groupby仅检查连续的元素
    print(date)
    for i in items:
        print(' ', i)
#%%
from collections import defaultdict

rows_by_date = defaultdict(list)  #构建多值字典
for row in rows:
    rows_by_date[row['date']].append(row)
for r in rows_by_date['07/01/2012']:
    print(r)
#%%
#1.16 过滤序列元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)
#%%
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
ivals
#%%
# itertools.compress()
# iterable 对象中对应选择器为 True 的元素
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
#%%
#1.17 从字典中提取子集

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
p1
p1 = dict((key, value) for key, value in prices.items() if value > 200)
#%%
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
p2
p2 = {key: prices[key] for key in prices.keys() & tech_names}
#%%
#1.18 映射名称到序列元素 collections.namedtuple()

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub
sub.addr
#%%
addr, joined = sub
addr, joined
#%%
#1.19 转换并同时计算数据

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
s
#%%
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
min_shares
#%%
#1.20 合并多个字典或映射

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
from collections import ChainMap

c = ChainMap(a, b)
#如果出现重复键，那么第一次出现的映射值会被返回
list(c.values())
#对于字典的更新或删除操作总是影响的是列表中第一个字典
c['z'] = 10
c['w'] = 40
a
del c['y']