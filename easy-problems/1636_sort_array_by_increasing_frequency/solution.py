def frequencySort(nums):
    final_dict = dict()
    for num in set(nums):
        final_dict[num] = nums.count(num)
    
    print(sorted(final_dict.items(), key=lambda x:x[1], reverse=True))


def main():
    testcases = [[1,1,2,2,2,3], [2,3,1,3,2], [-1,1,-6,4,5,-6,1,4,1]]
    for testcase in testcases:
        print(frequencySort(testcase))
        
if __name__ == "__main__":
    main()