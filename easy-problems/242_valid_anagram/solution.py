from collections import Counter

def isAnagram(s, t):
    return dict(sorted(Counter(s).items())) == dict(sorted(Counter(t).items()))
    

def main():
    testcases = [["anagram", "nagaram"], ["rat", "car"]]
    
    for testcase in testcases:
        print(isAnagram(testcase[0], testcase[1]))
        
if __name__ == "__main__":
    main()