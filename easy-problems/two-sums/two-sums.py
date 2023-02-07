from itertools import count


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexer = 1
    for element in nums:
        if (target-element) in nums[indexer:]:
            if nums.count(target-element)> 1 : 
                return [nums.index(target-element),nums.index(element, (nums.index(element) + 1))]
            else : 
                return [nums.index(element), nums.index(target-element)]
        indexer+=1
    return -1

if __name__ == "__main__":
    nums = [2,7,11,5]
    target = 9
    x = twoSum(nums, target)
    print(x)
