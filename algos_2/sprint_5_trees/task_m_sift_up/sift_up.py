def sift_up(head: Node) -> bool:

    res1 = True
    res2 = True

    if head.left is not None:
        if head.left.value >= head.value:
            return False
        else:
            res1 = sift_up(head.left)

    if head.right is not None:
        if head.right.value <= head.value:
            return False
        else:
            res2 = sift_up(head.right)

    return res1 and res2