"""
Посылка № = 34078207 (2020.09.05 23:16:31)все посылки контеста
Вердикт	Wrong answer
Контест	19312: Яндекс.Практикум, Алгоритмы: Спринт 7, графы
Задача	B: BFS
Participant	AntiRSI2
Компилятор	Python 3.7.3
"""

from collections import deque

# filename = 'task_b_11.txt'
filename = 'input.txt'

def bfs(name):
    searched = set()
    search_queue = deque()
    search_queue.append(name)
    searched.add(name)
    # print(search_queue)
    while search_queue:
        v = search_queue.popleft()
        # print('v', v)
        print(v, end=" ")
        if graph.get(v):
            for e in graph[v]:
                if e not in searched:
                    search_queue.append(e)
                    searched.add(e)
        else:
            searched.add(v)

f = open(filename)

n, m = list(map(int, f.readline().split()))
graph = {}

for _ in range(m):
    x, y = map(int, f.readline().split())
    if not graph.get(x):
        graph[x] = []
    if not graph.get(y):
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)

s = int(f.readline())

for k, v in graph.items():
    graph[k] = sorted(v)

bfs(s)