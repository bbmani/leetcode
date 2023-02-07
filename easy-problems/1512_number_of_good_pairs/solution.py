import math

def counter(arr):
    final_length = 0
    for i in range(0, len(arr)):
        if i == len(arr):
            break
        else:
            final_length += len(arr[i+1:])
    
    return final_length

def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # BASE CASES
    if len(set(nums)) == len(nums):
        return 0
    elif len(set(nums)) == 1:
        return int(math.factorial(len(nums)) / len(nums))
    else:
        final_dict = dict()
        for i in range(0, len(nums)):
            if nums[i] not in final_dict:
                final_dict[nums[i]] = [i]
            else:
                final_dict[nums[i]].append(i)
        return_value = 0
        print(final_dict)
        for key, value in final_dict.items():
            if len(value) > 1:
                return_value += counter(value)
                print("For Value : {}, the return value is {}".format(value, counter(value)))
        
    return return_value

def main():
    nums = [4,6,5,2,3,2,2,5,3,3,6,1,2]
    print(numIdenticalPairs(nums=nums))
    
if __name__ == "__main__":
    main()