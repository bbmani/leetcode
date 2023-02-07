from math import floor
import math


def search(nums: int, target: int):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    mid = math.floor(len(nums) / 2)
    final_answer = 0
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return search(nums[0:mid], target)
    elif nums[mid] < target:
        return search(nums[mid:len(nums)], target)


if __name__ == "__main__":
    print("Hello")
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    x = search(nums, target)
    print(x)
