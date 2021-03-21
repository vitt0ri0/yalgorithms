filename = 'input.txt'
# filename = '01'
# filename = '02'
# filename = '03'
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
            #
            # if gr.get(b):
            #     gr[b].append(a)
            # else:
            #     gr[b] = [a]

            edges_num -= 1
        # sort graph lists
        for node, neighbours in gr.items():
            neighbours.sort()

        # read start node
        start_node = 1

        return gr, start_node, visited


def dfs(gr, start, visited, result, topo_sort):
    """
    resursion for DFS
    """

    result.append(str(start))
    visited[start] = 1
    next_nodes = gr.get(start)
    if next_nodes:
        for el in next_nodes:
            if el != 0 and visited[el] != 1:
                dfs(gr, el, visited, result, topo_sort)

    # лучше вставлять в конец, и потом инвертировать список
    # topo_sort.insert(0, str(start))

    topo_sort.append(str(start))


def topological_sort(gr, start, visited):
    result = list()
    topo_sort = list()

    for i in range(1, len(visited)):
        if not visited[i]:
            dfs(gr, i, visited, result, topo_sort)
    return result, reversed(topo_sort)



if __name__ == '__main__':
    gr, start_node, visited = read_data()
    res, topo_sort = topological_sort(gr, start_node, visited)
    print(' '.join(topo_sort))
