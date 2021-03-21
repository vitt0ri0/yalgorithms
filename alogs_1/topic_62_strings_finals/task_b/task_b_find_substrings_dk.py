from collections import deque

# filename = '01'
filename = '09'

class Node:
    def __init__(self):
        self.next = {}
        self.word = []
        self.suffix = None

def ac_automate(patterns):

    root = Node()
    for path in patterns:
        node = root
        for symbol in path:
            node = node.next.setdefault(symbol, Node())
        node.word.append(path)

    queue = deque()
    for node in root.next.values():
        queue.append(node)
        node.suffix = root
    while len(queue) > 0:
        rnode = queue.popleft()

        for key, unode in rnode.next.items():
            queue.append(unode)
            fnode = rnode.suffix
            while fnode is not None and key not in fnode.next:
                fnode = fnode.suffix
            unode.suffix = fnode.next[key] if fnode else root
            unode.word += unode.suffix.word
            if len(unode.word) > 0:
                print(1)
            a = 1
    return root

def ac_run(text, templates):
    result = {}
    root = ac_automate(templates)
    node = root
    for i in range(len(text)):
        while node is not None and text[i] not in node.next:
            node = node.suffix
        if node is None:
            node = root
            continue
        node = node.next[text[i]]
        for pattern in node.word:
            if pattern not in result:
                result[pattern] = [i - len(pattern) + 2]
            else:
                result[pattern].append(i - len(pattern) + 2)
    return result

if __name__ == '__main__':
    with open(filename) as f:
        input_data = f.readlines()
    text = input_data[0].strip()
    n = int(input_data[1])
    templates = []
    for i in range(2,n+2):
        templates.append(input_data[i].strip())
    result = ac_run(text, set(templates))
    for templ in templates:
        print (templ, ' '.join([str(i) for i in result.get(templ,'')]))