from collections import deque


def read_data(filename):
    """
    Basic read_data for DFS and BFS
    """

    with open(filename) as f:

        nodes_num, edges_num = map(int, f.readline().split())
        gr = dict()
        visited = [0] * (nodes_num + 1)

        # read graph
        while edges_num > 0:
            a, b = map(int, f.readline().split())

            aa = gr.get(a)
            if aa:
                gr[a].append(b)
            else:
                gr[a] = [b]

            bb = gr.get(b)
            if bb:
                gr[b].append(a)
            else:
                gr[b] = [a]

            edges_num -= 1
        # sort graph lists
        for node, neighbours in gr.items():
            neighbours.sort(reverse=True)

        # read start node
        start_node = int(f.readline())

        return gr, start_node, visited


def dfs(gr, start, visited):
    """
    resursion for DFS
    """
    result = list()
    q = deque()
    q.append(start)

    while len(q) > 0:
        pos = q.pop()

        if visited[pos] == 0:
            result.append(str(pos))
        visited[pos] = 1

        next_nodes = gr.get(pos)

        if next_nodes:
            for el in next_nodes:
                if visited[el] != 1:
                    q.append(el)
                    visited[pos] = 1

    return result


def bfs(gr, start, visited):
    """
    """
    result = list()
    q = deque()
    q.append(start)
    visited[start] = 1

    while len(q) > 0:
        start = q.popleft()

        result.append(str(start))
        next_nodes = gr.get(start, None)

        if next_nodes:
            for el in next_nodes:
                if el != 0 and visited[el] != 1:
                    visited[el] = 1
                    q.append(el)

    return result
