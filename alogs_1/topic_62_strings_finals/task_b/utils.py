class Node:

    number = 0

    def __init__(self, *, is_root: bool = False, parent=None):
        self.is_final: bool = False
        self.words = list()

        self.letters: dict = dict()
        self.suff_link = 0
        self.is_root = is_root

        self.number = Node.number
        Node.number += 1
        self.parent = 0

    def __repr__(self):
        return f'Node {self.number}; {self.letters.keys()}, {self.is_final}'


class Trie:

    def __init__(self):
        self.root: Node = Node(is_root=True)
        self.nodes = [self.root]

    def add_word(self, word):
        cur_node = self.root
        new_node = None
        for letter in word:
            new_node = cur_node.letters.get(letter, None)
            if not new_node:
                new_node = Node(parent=cur_node)
                self.nodes.append(new_node)
                cur_node.letters[letter] = new_node

                # find suff link
                suff_link_node = None

                while not suff_link_node:
                    grand_parent_node = cur_node.suff_link
                    if grand_parent_node == 0:
                        new_node.suff_link = self.root
                        break

                    suff_link_node = grand_parent_node.letters.get(letter, None)

                    if suff_link_node:
                        new_node.suff_link = suff_link_node
                        break
                    if grand_parent_node == self.root:
                        new_node.suff_link = self.root
                        break
                    cur_node = cur_node.suff_link

            cur_node = new_node
        new_node.is_final = True
        new_node.words = [word]
        new_node.words.extend(new_node.suff_link.words)



    def check_string(self, string):
        pass


def check_string(trie: Trie, string: str):

    cur_node = trie.root
    result = dict()

    for pos, letter in enumerate(string):
        next_node = None
        while not next_node:
            next_node: Node = cur_node.letters.get(letter, None)
            if next_node:
                if next_node.is_final:
                    for found_word in next_node.words:
                        word_start_pos = pos + 2 - len(found_word)
                        res_word = result.get(found_word)
                        if not res_word:
                            result[found_word] = [word_start_pos]
                        else:
                            result[found_word].append(word_start_pos)
                break
            elif cur_node.is_root:
                break
            else:
                cur_node = cur_node.suff_link
        cur_node = next_node or trie.root

    return result

filename = 'input.txt'
# filename = '01'
# filename = '02'
# filename = '011'
# filename = '06'
filename = '09'

def read_data(filename):
    """
    Basic read_data for DFS and BFS
    """

    with open(filename) as f:

        the_string = f.readline().strip()
        num_words = int(f.readline())

        words = []
        for i in range(num_words):
            words.append(f.readline().strip())

        return the_string, num_words, words


if __name__ == '__main__':
    string, num, words = read_data(filename)

    t = Trie()
    for word in words:
        t.add_word(word.strip())

    result = check_string(t, string)
    for word in words:
        if word in result:
            result[word].sort()
        else:
            result[word] = list()
        print(f'{word} {" ".join(map(str, result[word]))}')





