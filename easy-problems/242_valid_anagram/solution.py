from collections import Counter

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_counter = dict(sorted(Counter(s).items()))
    t_counter = dict(sorted(Counter(t).items()))
    
    return s_counter == t_counter
    

def main():
    testcases = [["anagram", "nagaram"], ["rat", "car"]]
    
    for testcase in testcases:
        print(isAnagram(testcase[0], testcase[1]))
        
if __name__ == "__main__":
    main()