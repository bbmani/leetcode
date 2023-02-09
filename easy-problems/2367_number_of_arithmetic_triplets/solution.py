def arithmeticTriplets(nums, diff):
    total_count = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[j] - nums[i] == diff:
                for k in range(j, len(nums)):
                    if nums[k] - nums[j] == diff:
                        total_count += 1    
    return total_count

def main():
    testcases = [[[0,1,4,6,7,10], 3], [[4,5,6,7,8,9],2]]
    for testcase in testcases:
        return_value = arithmeticTriplets(testcase[0], testcase[1])
        print(return_value)
        
if __name__ == "__main__":
    main()