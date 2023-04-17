def shell_sort1(nums: list [int]) -> None:
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        gap //= 2


# n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

# shell_sort1(n)

# print(n)