import math

def gapGeneration(size: int):
    for i in range(size):
        for j in range(size):
            yield(int(math.pow(2, i) * math.pow(3, 1)))


def shell_sort3(nums: list [int]) -> None:
    gap = gapGeneration(len(nums))

    for i in (range(0, next(gap))):
        for j in range(i, len(nums)):
            temp = nums[j]
            a = j

            while (a >= i and temp < nums[a - i]):
                nums[a] = nums[a - i]
                a -= i

            nums[a] = temp


n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort3(n)

print(n)