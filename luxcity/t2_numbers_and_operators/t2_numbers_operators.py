import re

def solution(s: str):
    numbers = re.split('(\*|\-|\+)', s)

    results = recursive(numbers)

    results.sort()
    return results

    # print(results)

def recursive(parts: list, results: list = None, depth=0):
    """
    depth - we use it to count recursive depth for visualization purposes
    """
    if results is None:
        results = list()

    if len(parts) == 1:
        results.append(parts[0])
        return results

    for i in range(0, len(parts)-1, 2):
        sum = perform_operation(parts[i], parts[i+1], parts[i+2])

        new_parts = parts.copy()
        new_parts.pop(i)
        new_parts.pop(i)
        new_parts[i] = sum

        recursive(new_parts, results, depth + 1)

    return results


def perform_operation(a, operation, b):
    result = 'a'
    a = int(a)
    b = int(b)
    if operation == '*':
        result = a * b
    if operation == '+':
        result = a + b
    if operation == '-':
        result = a - b
    assert result != 'a'
    # result = str(result)
    return result


def solution_visualize(s: str):
    numbers = re.split('\*|\-|\+', s)
    results = recursive_visualization(numbers)
    for l in results:
        print(l)


def recursive_visualization(parts: list, results: set = None, depth=0):
    """
    depth - we use it to count recursive depth for visualization purposes
    """
    if results is None:
        results = set()

    if len(parts) == 1:
        results.add(parts[0])
        return results

    for i in range(len(parts)-1):
        sum = parts[i] + str(depth) + parts[i+1]

        new_parts = parts.copy()
        new_parts.pop(i)
        new_parts[i] = sum

        recursive_visualization(new_parts, results, depth + 1)

    return results


if __name__ == '__main__':
    s = "2*3-4*5"
    # s = "2*3+4"
    res = solution(s)
    print(res)
    # print(res)
    # test()