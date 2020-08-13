def task_f(st1, st2):
    d1 = dict()
    d2 = dict()
    for el1, el2 in zip(st1, st2):
        if el1 in d1:
            if d1[el1] != el2:
                return False
        else:
            d1[el1] = el2
        if el2 in d2:
            if d2[el2] != el1:
                return False
        else:
            d2[el2] = el1
    return True

