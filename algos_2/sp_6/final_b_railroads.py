import sys


def dfs(graph, n) -> bool:
    verticies = list(range(n))
    visited = [False] * n
    stack = []
    on_stack = [False] * n

    for v in verticies:
        if visited[v]:
            continue
        stack.append(v)

        while len(stack):
            s = stack[-1]

            if not visited[s]:
                visited[s] = True
                on_stack[s] = True
            else:
                on_stack[s] = False
                stack.pop()

            for w in graph[s]:
                if not visited[w]:
                    stack.append(w)
                elif on_stack[w]:
                    return True

    return False


def solution():
    n = int(sys.stdin.readline())

    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        symbols_count = n - i - 1
        railways = list(sys.stdin.readline())
        for j in range(i + 1, i + symbols_count + 1):
            symbol = railways[j - i - 1]
            if symbol == 'B':
                graph[i].append(j)
            else:
                graph[j].append(i)

    has_cycle = dfs(graph, n)
    print('NO' if has_cycle else 'YES')

solution()