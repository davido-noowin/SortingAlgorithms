def genGap(size : int) -> list [int]:
    stack = [1]
    i = 0
    j = 0
    while (i <= size and j <= size):
        multiple_of_2 = 2 * stack[i]
        multiple_of_3 = 3 * stack[j]
        minimum = min(multiple_of_2, multiple_of_3)
        stack.append(minimum)
        if multiple_of_2 <= multiple_of_3:
            i += 1
        if multiple_of_2 >= multiple_of_3:
            j += 1

    return stack


def shell_sort3(nums: list [int]) -> None:
    r = genGap(len(nums))
    gap = r.pop()

    while len(r) > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        gap = r.pop()


# n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

# shell_sort3(n)

# print(n)