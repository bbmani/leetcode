def calculateTime(keyboard, word):
    """
    :type keyboard: str
    :type word: str
    :rtype: int
    """
    final_dict = dict()
    for i in range(0, len(keyboard)):
        final_dict[keyboard[i]] = int(i)
    
    total_distance = 0
    total_distance += final_dict[word[0]]
    
    for i in range(1, len(word)):
        total_distance += abs(final_dict[word[i-1]] - final_dict[word[i]])
        
    return total_distance
    

def main():    
    testcases = [["abcdefghijklmnopqrstuvwxyz", "cba"],["pqrstuvwxyzabcdefghijklmno", "leetcode"]]
    
    for testcase in testcases:
        keyboard, word = testcase[0], testcase[1]
        returnValue = calculateTime(keyboard=keyboard, word=word)
        print("The result for testcase {} : {}".format(testcase, returnValue)) 
    
    
if __name__ == "__main__":
    main()