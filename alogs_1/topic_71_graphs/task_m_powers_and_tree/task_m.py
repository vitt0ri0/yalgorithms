filename = '08'

# filename = 'input.txt'


def read_data():
    with open(filename) as f:
        nodes_num = int(f.readline().strip())

        powers = list(map(int, f.readline().split()))
        powers.insert(0, 0)

        return nodes_num, powers


def add_edges_both(gr, a, b):
    if gr.get(a):
        gr[a].append(b)
    else:
        gr[a] = [b]

    if gr.get(b):
        gr[b].append(a)
    else:
        gr[b] = [a]


def make_graph(nodes_num, powers):
    gr = dict()
    for i in range(1, nodes_num + 1):
        for j in range(i+1, nodes_num + 1):
            if powers[i] > 0:
                power2 = powers.copy()
                add_edges_both(gr, i, j)
                powers[i] -= 1
                powers[j] -= 1
                pass
            else:
                break
        if sum(powers) == 0:
            break
    return gr


def dfs(gr, start, nodes_num, parent=None, visited=None):
    """
    resursion for DFS
    """
    visited = visited or [0] * (nodes_num + 1)

    visited[start] = 1

    next_nodes = gr.get(start)
    if next_nodes:
        for el in next_nodes:
            if el != 0 and el != parent:
                if visited[el] == 1:
                    return False
                return dfs(gr, el, nodes_num, start, visited)

    return True


if __name__ == '__main__':
    nodes_num, powers = read_data()
    gr = make_graph(nodes_num, powers)
    result = dfs(gr, 1, nodes_num)

    print('YES') if result else print('NO')
