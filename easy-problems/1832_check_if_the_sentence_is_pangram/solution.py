def checkIfPangram(sentence):
    alphabets = set()
    for i in range(97, 123):
        alphabets.add(chr(i))
    
    return alphabets == set(sentence)

def main():
    testcases = ["thequickbrownfoxjumpsoverthelazydog", "leetcode"]
    for testcase in testcases:
        return_value = checkIfPangram(testcase)
        print(return_value)
        
if __name__ == "__main__":
    main()