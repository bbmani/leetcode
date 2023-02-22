def missingNumber(nums):
    return list(set([i for i in range(0, len(nums) + 1)]) - set(nums))[0]

def main():
    testcases = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1]]
    for testcase in testcases:
        print(missingNumber(testcase))

if __name__ == "__main__":
    main()