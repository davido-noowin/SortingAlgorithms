from insertion_sort import insertion_sort
from merge_sort import merge
# import random

half = -1

def hybrid_sort1(nums: list[int]) -> None:
    current_size = len(nums)

    global half
    if (half == -1):
        half = int(current_size ** (1/2))

    if (current_size > half):
        num1 = nums[0:len(nums)//2]
        num2 = nums[len(nums)//2:len(nums)]

        hybrid_sort1(num1)
        hybrid_sort1(num2)

        new_list = nums.copy()
        merge(new_list, num1, num2)

        for i in range(len(new_list)):
            nums[i] = new_list[i]
    else:
        insertion_sort(nums)


'''
n = [i for i in range(9000)]
random.shuffle(n)
hybrid_sort1(n)

with open('hybrid_sort1_test.txt', 'w') as f:
    for i in n:
        f.write(str(i) + '\n')
'''