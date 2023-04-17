# import random
import math

def gapGeneration(maximum: int) -> list [int]:
    stack = []
    size = 0
    gap = -1
    while (gap <= maximum):
        if size % 2 == 0:
            gap = 9 * (2 ** size) - 9 * 2 ** (size / 2) + 1
        else:
            gap = 8 * (2 ** size) - 6 * 2 ** ((size + 1) / 2) + 1

        if (gap > maximum):
            break

        stack.append(int(gap))
        size += 1

    return stack


def shell_sort4(nums: list [int]) -> None:
    length = len(nums)
    r = gapGeneration(length)
    print(r)
    gap = r.pop()

    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp
        
        if (len(r) > 0):
            gap = r.pop()
        else:
            break


'''
n = [i for i in range(9000)]
random.shuffle(n)
shell_sort4(n)

with open('shell_sort4_test.txt', 'w') as f:
    for i in n:
        f.write(str(i) + '\n')
'''