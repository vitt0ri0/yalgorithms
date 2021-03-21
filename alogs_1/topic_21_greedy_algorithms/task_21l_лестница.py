def task21l_rec(nums, i=0, sh=0, debug=False, debug2=False, visited=set()):
    #if i in visited:
    #    return False
    if i >= len(nums):
        return True
    el = nums[i]
    if debug:
        print(f'_{sh}_ ({i}) {el}')
    if el == 0:
        visited.add(i)
        return False
    result = []
    sh += 1

    for j in range(el, 0, -1):
        res = task21l_rec(nums, i+j, sh, debug=debug, debug2=debug2, visited=visited)
        if res:
            return True
    if debug2:
        input()
    visited.add(i)
    return False