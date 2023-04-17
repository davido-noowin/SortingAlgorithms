import math
# import random

def shell_sort2(nums: list [int]) -> None:
    seen_one = False
    gap = math.pow(2, math.log2(len(nums))) + 1
    gap = int(gap)
    
    while gap > 0:
        if gap == 1:
            seen_one = True
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        gap = ((gap - 1) // 2) + 1
        if seen_one:
            break


'''
n = [i for i in range(1000)]
random.shuffle(n)
shell_sort2(n)

with open('shell_sort2_test.txt', 'w') as f:
    for i in n:
        f.write(str(i) + '\n')
'''