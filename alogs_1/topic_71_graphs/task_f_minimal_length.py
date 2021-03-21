from collections import deque

filename = 'input.txt'
# filename = 'task_a_test_1.txt'
# filename = 'task_f_01.txt'
# filename = 'task_f_02.txt'
# filename = 'task_f_03.txt'


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
        # start_node, finish_node = map(int, f.readline().split())

        start_node, finish_node = map(int, f.readline().split())

        return gr, start_node, visited, finish_node


def bfs(gr, start, visited, finish):
    """
    """
    depth = 0

    if start == finish:
        return depth

    result = list()
    q = deque()
    # we store element AND its' depth while BFS-ing our graph
    q.append((start, depth))
    visited[start] = 1

    while len(q) > 0:
        start, depth = q.popleft()
        depth += 1

        result.append((start, depth))
        next_nodes = gr.get(start, None)

        if next_nodes:
            for el in next_nodes:
                if el != 0 and visited[el] != 1:
                    # we stop if we find the Finish element and return it's depth
                    if el == finish:
                        return depth
                    visited[el] = 1
                    q.append((el, depth))

    return -1


if __name__ == '__main__':
    gr, start, visited, finish = read_data(filename)
    depth = bfs(gr, start, visited, finish)
    print(depth)
