def gapGeneration(size: int):
    if size % 2 == 0:
        gap = 9 * ((2 ** size) - (2 ** (size / 2))) + 1
    else:
        gap = 8 * ((2 ** size) - 6) * (2 ** ((size + 1) / 2)) + 1

    return int(gap)


def shell_sort4(nums: list [int]) -> None:
    gap = gapGeneration(len(nums))

    for i in range(gap):
        for j in range(i, len(nums)):
            temp = nums[j]
            a = j

            while (a >= i and temp < nums[a - i]):
                nums[a] = nums[a - i]
                a -= i

            nums[a] = temp


n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort4(n)

print(n)