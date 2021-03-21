"""
Посылка № = 34079525 (2020.09.06 01:01:52)все посылки контеста
Вердикт	Wrong answer
Контест	19312: Яндекс.Практикум, Алгоритмы: Спринт 7, графы
Задача	D: Топологическая сортировка
Participant	AntiRSI2
Компилятор	Python 3.7.3
"""


visited = []
result = []
graph = {}


def dfs(start):
    visited.append(start)
    if graph.get(start):
        for u in graph[start]:
            if u not in visited:
                dfs(u)
    result.append(start)


n, m = list(map(int, input().split()))

for _ in range(m):
    u, v = list(input().split())
    if not graph.get(u):
        graph[u] = []
    graph[u].append(v)

for i in range(1, n + 1):
    if str(i) not in visited:
        dfs(str(i))

print(*result)