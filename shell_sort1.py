def shell_sort1(nums: list [int]) -> None:
    gap = len(nums) // 2

    for i in reversed(range(0, gap)):
        for j in range(i, len(nums)):
            temp = nums[j]
            a = j

            while (a >= i and temp < nums[a - i]):
                nums[a] = nums[a - i]
                a -= i

            nums[a] = temp

        i //= 2


n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort1(n)

print(n)