from collections import Counter

def groupAnagrams(strs):
    # BASE CASE
    if len(strs) == 1 or len(set(strs)) == 1:
        return [strs]

    # NORMAL CASE
    final_list = list()
    while len(strs) != 0:
        temp_value = strs[0]
        temp_list = list()
        temp_list.append(temp_value)
        for value in strs[1:]:
            if dict(sorted(Counter(value).items())) == dict(sorted(Counter(temp_value).items())):
                temp_list.append(value)
        for value in temp_list:
            strs.remove(value)
        final_list.append(temp_list)            
    
    return final_list        

def main():
    testcases = [["eat","tea","tan","ate","nat","bat"], [""], ["a"],["","",""],["ate","eat","tea"]]
    for testcase in testcases:
        print(groupAnagrams(testcase))
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    #  