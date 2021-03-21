# filename = 'task_a_test_1.txt'
filename = 'input.txt'
# filename = 'task_a_05.txt'
filename = '01my'
filename = '02fin_b01'
# filename = '03fin_b02'

import sys
sys.setrecursionlimit(10**5)

"""
Вариант, с хранением графа в виде списков смежности.
"""


def read_data():
    with open(filename) as f:
        nodes_num, edges_num = map(int, f.readline().split())
        gr = dict()

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

        start_node = 1
        visited = [0] * (nodes_num + 1)

        return gr, start_node, visited


def dfs(gr, start, visited):

    result = list()
    start = 1

    dfs_inner(gr, visited, start=start, result=result)

    return result


def dfs_inner(gr, visited, *, parent=None, start=1, result=None, visited_num=0):
    """
    resursion for DFS
    """
    visited_num += 1

    # result.append(str(start))

    num = visited_num
    visited[start] = num  # coloring grey (started traversal)

    min_weight = visited_num
    next_nodes = gr.get(start)
    if next_nodes:
        for el in next_nodes:

            # for ell in next_nodes:
            #     if ell != parent and visited[ell] != 0:
            #         min_weight = min(min_weight, visited[ell])

            if el != 0 and visited[el] == 0:
                res = dfs_inner(gr, visited, parent=start, start=el, result=result, visited_num=visited_num)
                # for ell in next_nodes:
                #     if ell != parent and visited[ell] != 0:
                #         min_weight = min(min_weight, visited[ell])
                if res > num:
                    result.append((start, el))

                min_weight = min(res, min_weight)

        for ell in next_nodes:
            if ell != parent and visited[ell] != 0:
                min_weight = min(min_weight, visited[ell])

                # num = res  # updating color (updating traversal order)

    visited[start] = visited_num  # coloring black (finished traversal)

    return min_weight


if __name__ == '__main__':
    gr, start_node, visited = read_data()
    result = dfs(gr, start_node, visited)
    print(result)
