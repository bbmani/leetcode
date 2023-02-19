def myAtoi(s):
    return 1

def main():
    testcases = ["42", "   -42", "4193 with words"]
    for testcase in testcases:
        returnValue = myAtoi(testcase)
        print(returnValue)
        
if __name__ == "__main__":
    main()