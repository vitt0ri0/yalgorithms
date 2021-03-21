class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(head: Node) -> bool:

    res1 = True
    res2 = True

    if head.left is not None:
        if head.left.value >= head.value:
            return False
        else:
            res1 = solution(head.left)

    if head.right is not None:
        if head.right.value <= head.value:
            return False
        else:
            res2 = solution(head.right)

    return res1 and res2
