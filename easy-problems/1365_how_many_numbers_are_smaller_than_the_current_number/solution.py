def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    final_list = list()
    # BASE CASE
    if len(set(nums)) == 1:
        for i in range(len(nums)):
            final_list.append(0)
        return final_list
    else:    
        for num in nums:
            returnValue = 0
            returnValue += len([small for small in nums if small < num])
            final_list.append(returnValue)
        
        return final_list

def main():
    testcases = [[8,1,2,2,3],[6,5,4,8],[7,7,7,7]]
    for testcase in testcases:
        returnValue = smallerNumbersThanCurrent(testcase)
        print("The result for testcase {} is {}".format(testcase, returnValue))
        
if __name__ == "__main__":
    main()