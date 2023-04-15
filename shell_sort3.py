import math


def shell_sort3(nums: list [int]) -> None:
    size = len(nums)
    i = size
    j = size
    gap = (int(math.pow(2, size) * math.pow(3, size)))

    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        min_num = -1

        max_num_2 = (int(math.pow(2, i-1) * math.pow(3, j)))
        max_num_3 = (int(math.pow(2, i) * math.pow(3, j-1)))

        gap = max(max_num_2, max_num_3)
        min_num = min(max_num_2, max_num_3)
        



n = [1, 6, 14] #, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort3(n)

print(n)