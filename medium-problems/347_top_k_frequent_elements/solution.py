from collections import Counter

def topKfrequent(nums, k):
    if k == len(nums):
            return nums
        
    final_dict = dict(Counter(nums))
    final_dict = dict(sorted(final_dict.items(), key=lambda x:x[1], reverse=True))
    return list(final_dict)[:k]

def main():
    testcases = [[1,1,1,2,2,3], [1]]
    for testcase in testcases:
        print(topKfrequent(testcase))

if __name__ == "__main__" :
    main()