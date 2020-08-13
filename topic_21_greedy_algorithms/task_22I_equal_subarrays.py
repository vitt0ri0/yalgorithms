# n = int(input())
# arr = list(map(int, input().split()))
def balancedSplitExists(nums):
        if len(nums)<=1:
            return False
        if len(nums)==2:
            return nums[0]==nums[1]
        #
        nums = sorted(nums)
        print(f'sorted: {nums}')
        #
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        set_sums = {0}

        for x in nums:
#             print("x", x)
            print(f'current x: {x}')
            new = set()
            for s in set_sums:
                # print('current ')
                if (s+x)==target:
                    print(f'True: {s}+{x}')

                    return True
                print(f'current s: {s}; new add {s} + {x}')
                new.add(s+x)

            print(f'x: {x}, set_sums: {set_sums}, new: {new}')
            set_sums |= new
            print(f'set sums became {set_sums}')
            print('...................')

        return False

# print(balancedSplitExists(arr))


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 5]
    res = balancedSplitExists(nums)
    print(res)