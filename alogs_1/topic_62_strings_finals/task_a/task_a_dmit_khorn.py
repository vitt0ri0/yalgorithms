filename = 'input.txt'
filename = '01'
# filename = '02'

def palindrome(words):
    result = set()
    for word, index in words.items():
        for i in range (len(word)+1):
            left = word[:i]
            right = word[i:]
            if left == left[::-1] and words.get(right[::-1], -1) not in (index, -1):
                result.add( (words[right[::-1] ], index))
            if right == right[::-1] and words.get( left[::-1], -1) not in (index, -1):
                result.add( (index, words[ left[::-1] ] ) )
    return sorted(result)

if __name__ == '__main__':
    with open(filename,'r') as f:
        input_data = f.readlines()
    n = int(input_data[0])
    words = dict()
    for i in range(1,n+1):
        words[input_data[i].strip()] = i
    for elem in palindrome(words):
        print (elem[0], elem[1])