def insertion_sort(nums : list [int]) -> None:
    for first_index in range(len(nums)):
        temp = nums[first_index]

        second_index = first_index

        while (second_index > 0 and nums[second_index - 1] > temp):
            nums[second_index] = nums[second_index - 1]
            second_index -= 1

        nums[second_index] = temp