from functools import reduce
def productExceptSelf(nums):
    final_list = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        final_list[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        final_list[i] *= postfix
        postfix *= nums[i]
    
    return final_list

def main():
    testcases = [[1,2,3,4], [-1,1,0,-3,3]]
    for testcase in testcases:
        print(productExceptSelf(testcase))
        
if __name__ == "__main__" : 
    main()