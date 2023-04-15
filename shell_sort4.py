def gapGeneration(size: int):
    if size % 2 == 0:
        gap = 9 * (2 ** size) - 9 * 2 ** (size / 2) + 1
    else:
        gap = 8 * (2 ** size) - 6 * 2 ** ((size + 1) / 2) + 1

    return int(gap)


def shell_sort4(nums: list [int]) -> None:
    length = len(nums)
    gap = gapGeneration(length)

    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp
        
        length -= 1
        gap = gapGeneration(length)


n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort4(n)

print(n)