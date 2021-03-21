filename = 'input.txt'
# filename = 'task_h_01.txt'
# filename = 'task_h_02.txt'
filename = 'task_h_36.txt'


def read_data_and_check_if_graph_is_full(filename):
    """
    Basic read_data for DFS and BFS
    """

    with open(filename) as f:

        nodes_num, edges_num = map(int, f.readline().split())
        gr = dict()
        visited = [0] * (nodes_num + 1)

        if edges_num == 0 and nodes_num > 1:
            return False

        # read graph
        while edges_num > 0:
            a, b = map(int, f.readline().split())

            if a != b:
                aa = gr.get(a)
                if aa:
                    gr[a].add(b)
                else:
                    gr[a] = {b}

                bb = gr.get(b)
                if bb:
                    gr[b].add(a)
                else:
                    gr[b] = {a}

            edges_num -= 1
        # sort graph lists
        if not gr:
            return False

        for node, neighbours in gr.items():
            if len(neighbours) <= nodes_num - 1:
                return False

        return True


if __name__ == '__main__':
    result = read_data_and_check_if_graph_is_full(filename)
    print('YES') if result else print('NO')
