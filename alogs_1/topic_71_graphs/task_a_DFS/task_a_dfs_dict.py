from collections import deque

filename = 'input.txt'
# filename = 'task_a_test_1.txt'
# filename = 'task_a_05.txt'

"""
Первый вариант, с хранением графа в виде матрицы смежности. 
"""


def read_data():

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


if __name__ == '__main__':
    gr, start_node, visited = read_data()
    res = dfs(gr, start_node, visited)
    print(' '.join(res))
