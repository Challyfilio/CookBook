#%%1.1 将序列分解为单独的变量
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, b, c, _=data#_占位
b,c
#%%1.2 解压可迭代对象赋值给多个变量
data = ['ACME', 50, 91.1, (2012, 12, 21)]
a,*b,c=data
b
#%%1.3 保留最后 N 个元素 collections.deque
from collections import deque
q=deque()
q.append(1)
q.append(2)
q.append(3)
q
q.appendleft(4)
q
q.pop()
q
q.popleft()
#%%1.4 查找最大或最小的 N 个元素 nlargest() nsmallest()
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(11,nums)
heapq.nsmallest(11,nums)
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
cheap,expensive
#%%1.5 实现一个优先级队列 PriorityQueue()
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
a > b,b > c,a == c
#%%1.6 字典中的键映射多个值 collections  defaultdict
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
d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d
#%%1.7 字典排序 collections  OrderedDict
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
#%%1.8 字典的运算
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
#%%1.9 查找两字典的相同点
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
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
c
#%%1.10 删除序列相同元素并保持顺序
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
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
list(dedupe(a, key=lambda d: d['x']))