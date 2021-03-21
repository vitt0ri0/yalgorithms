filename = 'input.txt'
# filename = '01'
# filename = '02'
# filename = '03'
# filename = '04'
filename = '06'
import sys
sys.setrecursionlimit(10**5)

"""
Вариант, с хранением графа в виде списков смежности.
"""


def read_data():
    with open(filename) as f:
        nodes_num, edges_num = map(int, f.readline().split())
        gr = dict()
        gr2 = dict()
        visited = [0] * (nodes_num + 1)

        # read graph
        while edges_num > 0:
            a, b = map(int, f.readline().split())
            # собираем прямой граф
            if gr.get(a):
                gr[a].append(b)
            else:
                gr[a] = [b]

            # собираем инвертированный граф
            if gr2.get(b):
                gr2[b].append(a)
            else:
                gr2[b] = [a]

            edges_num -= 1
        # sort graph lists
        # for node, neighbours in gr.items():
        #     neighbours.sort()
        #
        # # sort graph lists
        # for node, neighbours in gr2.items():
        #     neighbours.sort()

        # read start node
        start_node = 1

        return gr, gr2, visited, nodes_num


def dfs(gr, start, visited, result=None, topo_sort=None, visited_color=1):
    """
    resursion for DFS
    """

    if result is not None:
        result.append(start)
    visited[start] = visited_color
    next_nodes = gr.get(start)
    if next_nodes:
        for el in next_nodes:
            if visited[el] == 0:
                dfs(gr, el, visited, result, topo_sort, visited_color)

    if topo_sort is not None:
        topo_sort.append(start)


def topological_sort(gr, visited):
    result = list()
    topo_sort = list()

    for node_num in range(1, len(visited)):
        if not visited[node_num]:
            dfs(gr, node_num, visited, result=result, topo_sort=topo_sort)
    return result, topo_sort


def connectivity_components(gr, nodes_num):
    visited = [0] * (nodes_num + 1)
    component_num = 0

    total_result = list()
    for node_num in reversed(topo_sort):
        if visited[node_num] == 0:
            result = list()
            dfs(gr, node_num, visited, result=result, visited_color=component_num + 1)
            total_result.append(sorted(result))
            component_num += 1

    return component_num, sorted(total_result)


if __name__ == '__main__':
    gr, gr2, visited, nodes_num = read_data()
    result, topo_sort = topological_sort(gr2, visited)
    gr2 = gr  # way of freeing memory
    num, total_result = connectivity_components(gr, nodes_num)
    print(num)
    # for line in total_result:
    #     print(' '.join(map(str, line)))