import math

def shell_sort2(nums: list [int]) -> None:
    gap = math.pow(2, math.log2(len(nums))) + 1
    gap = int(gap)

    
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        gap = ((gap - 1) // 2) + 1

        if (gap == 1):
            break



n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort2(n)

print(n)