# import random

def genGap(size : int) -> list [int]:
    stack = [1]
    i = 0
    j = 0
    count = 0
    while (count < size):
        multiple_of_2 = 2 * stack[i]
        multiple_of_3 = 3 * stack[j]
        minimum = min(multiple_of_2, multiple_of_3)
        stack.append(minimum)
        if multiple_of_2 <= multiple_of_3:
            i += 1
        if multiple_of_2 >= multiple_of_3:
            j += 1

        count += 1

        if (stack[-1] > size):
            stack.pop()
            break

    return stack


def shell_sort3(nums: list [int]) -> None:
    r = genGap(len(nums))
    # print(r)
    gap = r.pop()

    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            a = i

            while (a >= gap and temp < nums[a - gap]):
                nums[a] = nums[a - gap]
                a -= gap

            nums[a] = temp

        if (len(r) > 0):
            gap = r.pop()
        else:
            break


'''
n = [i for i in range(9000)]
random.shuffle(n)
shell_sort3(n)

with open('shell_sort3_test.txt', 'w') as f:
    for i in n:
        f.write(str(i) + '\n')
'''