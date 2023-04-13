from insertion_sort import insertion_sort
from merge_sort import merge

def hybrid_sort1(nums: list[int], H: int) -> None:
    current_size = len(nums)

    if (current_size > H):
        num1 = nums[0:len(nums)//2]
        num2 = nums[len(nums)//2:len(nums)]

        hybrid_sort1(num1, H)
        hybrid_sort1(num2, H)

        new_list = nums.copy()
        merge(new_list, num1, num2)

        for i in range(len(new_list)):
            nums[i] = new_list[i]
    else:
        insertion_sort(nums)

n = [1, 6, 14, 11, 2, 15, 21, 67, 3, 5, 19]

hybrid_sort1(n, len(n)//6)

print(n)