from collections import deque

filename = 'input.txt'
# filename = 'task_a_test_1.txt'
# filename = 'task_i_01.txt'

"""

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

        return gr, visited, nodes_num


def dfs(gr, start, visited):
    """
    queue for DFS
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


def count_join_components(gr: dict, visited, nodes_num):
    num_components = 0
    for v in range(1, nodes_num + 1):
        if visited[v] == 0:
            dfs(gr, v, visited)
            num_components += 1
    return num_components


if __name__ == '__main__':
    gr, visited, nodes_num = read_data()
    num_components = count_join_components(gr, visited, nodes_num)
    print(num_components)
