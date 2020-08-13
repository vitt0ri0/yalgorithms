base62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
base_len = len(base62)
res = [0]

def form_url_2(pos):
    ''' Фукнция формирования системы счисления по основанию base_len. При каждом вызове инкрементируем res, что и ялвяется нашим набором разрядов'''
    j = 0
    if pos == 0:
        res[j] = 0
        return '0'
    else:
        res[j] += 1
        while res[j] >= base_len:
            res[j] = 0
            j += 1
            if len(res) <= j:
                res.append(0)
            res[j] += 1

    num = ''.join(map(str, reversed(res)))
    num = [base62[i] for i in reversed(res)]
    while num[0] == base62[0]:
        num.pop(0)
    s = ''.join(num)
    return s


def solution(lines):

    d = {}

    pos = 0

    for line in lines:
        parts = line.split()
        if parts[0] == 'post':
            url = parts[1]
            a = url.find('//')
            b = url.find('.')

            base = form_url_2(pos)

            new_url = url[:a+2] + base + url[b:]
            pos += 1

            content = ' '.join(parts[2:])

            d[new_url] = content

            print(new_url)

        elif parts[0] == 'get':
            url = parts[1]

            content = d.get(url, None)
            if content:
                print(content)
            else:
                print('error')

        else:
            raise ValueError

    pass


def run_in_context():
    n = int(input())
    lines = [''] * n
    for i in range(n):
        lines[i] = input()
    return lines


def run_debug():
    filename = '52a_20'
    f = open(filename)
    n = int(f.readline())

    lines = [''] * n
    for i in range(n):
        lines[i] = f.readline()
    return lines


def test_form_num():
    global base62, base_len
    base62 = '0a'
    base_len = len(base62)
    for i in range(17):
        res = form_url_2(i)
        print(res)


if __name__ == '__main__':
    # lines = run_debug()
    lines = run_in_context()

    solution(lines)
    # test_form_num()
