def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My Solution
        '''
        nums_set = set(nums)
        for x in nums_set:
            if nums.count(x) == 1 :
                return x
        '''
        result = 0
        for x in nums:
            result = result ^ x
        return result
        
if __name__ == "__main__" :
    nums = [4,1,2,1,2]
    x = singleNumber(nums)
    print(x)