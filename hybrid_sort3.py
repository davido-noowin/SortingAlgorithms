from insertion_sort import insertion_sort
from merge_sort import merge

half = -1

def hybrid_sort3(nums: list[int]) -> None:
    current_size = len(nums)

    if (half == -1):
        half = current_size // 6

    if (current_size > half):
        num1 = nums[0:len(nums)//2]
        num2 = nums[len(nums)//2:len(nums)]

        hybrid_sort3(num1)
        hybrid_sort3(num2)

        new_list = nums.copy()
        merge(new_list, num1, num2)

        for i in range(len(new_list)):
            nums[i] = new_list[i]
    else:
        insertion_sort(nums)

# n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

# hybrid_sort3(n, len(n)//6)

# print(n)