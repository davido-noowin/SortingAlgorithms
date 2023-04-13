import math

def shell_sort2(nums: list [int]) -> None:
    gap = math.pow(2, math.log(len(nums), 2)) + 1
    gap = int(gap)

    count = 0
    for i in range(0, gap):
        for j in range(i, len(nums)):
            temp = nums[j]
            a = j

            while (a >= i and temp < nums[a - i]):
                nums[a] = nums[a - i]
                a -= i

            nums[a] = temp

        count += 1
        i = math.pow(2, count) + 1


n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

shell_sort2(n)

print(n)