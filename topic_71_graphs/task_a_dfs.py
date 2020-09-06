# filename = 'task_a_test_1.txt'
filename = 'input.txt'

"""
Первый вариант, с хранением графа в виде матрицы смежности. 
"""


def init_graph(nodes_num):
    l = nodes_num + 1
    g = [[0] * l for i in range(l)]
    return g


def read_data():
    with open(filename) as f:
        nodes_num, edges_num = map(int, f.readline().split())
        gr = init_graph(nodes_num)

        while edges_num > 0:
            a, b = map(int, f.readline().split())
            gr[a][b] = 1
            gr[b][a] = 1
            edges_num -= 1

        start_node = int(f.readline())

        visited = [0] * (nodes_num + 1)

        return gr, start_node, visited


def dfs(gr, start, visited):
    """
    DFS start
    """
    result = list()
    dfs_rec(gr, start, visited, result)
    return result


def dfs_rec(gr, start, visited, result):
    """
    resursion for DFS
    """
    result.append(str(start))
    visited[start] = 1
    next_nodes = gr[start]
    for pos, el in enumerate(next_nodes):
        if el != 0 and visited[pos] != 1:
            dfs_rec(gr, pos, visited, result)



if __name__ == '__main__':
    gr, start_node, visited = read_data()
    res = dfs(gr, start_node, visited)
    print(' '.join(res))
