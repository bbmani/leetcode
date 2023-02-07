import numpy as np

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    # adding the base case
    if target in nums:
      return nums.index(target)
    
    # final case
    for x in nums:
      if x > target:
        return nums.index(x)
    
    return len(nums)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 10
    x = searchInsert(nums, target)
    
    print(x)
