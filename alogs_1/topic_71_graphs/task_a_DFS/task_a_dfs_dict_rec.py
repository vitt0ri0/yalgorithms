# filename = 'task_a_test_1.txt'
filename = 'input.txt'
# filename = 'task_a_05.txt'
import sys
sys.setrecursionlimit(10**5)

"""
Вариант, с хранением графа в виде списков смежности.
"""


def read_data():
    with open(filename) as f:
        nodes_num, edges_num = map(int, f.readline().split())
        gr = dict()
        visited = [0] * (nodes_num + 1)

        # read graph
        while edges_num > 0:
            a, b = map(int, f.readline().split())
            if gr.get(a):
                gr[a].append(b)
            else:
                gr[a] = [b]

            if gr.get(b):
                gr[b].append(a)
            else:
                gr[b] = [a]

            edges_num -= 1
        # sort graph lists
        for node, neighbours in gr.items():
            neighbours.sort()

        # read start node
        start_node = int(f.readline())

        return gr, start_node, visited


def dfs(gr, start, visited, result=None):
    """
    resursion for DFS
    """
    result = result or list()

    result.append(str(start))
    visited[start] = 1
    next_nodes = gr.get(start)
    if next_nodes:
        for el in next_nodes:
            if el != 0 and visited[el] != 1:
                dfs(gr, el, visited, result)

    return result



if __name__ == '__main__':
    gr, start_node, visited = read_data()
    res = dfs(gr, start_node, visited)
    print(' '.join(res))
