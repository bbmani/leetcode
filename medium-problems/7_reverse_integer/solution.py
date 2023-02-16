def reverse(x):
    # positive integer (str rev and turn it into integer)
    
    final_value = 0
    if x >= 2**31-1 or x <= -2**31 or x == 0:
        return 0
    elif x > 0:
        final_value = int(str(x)[::-1])
        return 0 if final_value >= 2**31-1 or final_value <= -2**31 else final_value
    # negative integer 
    else:
        final_value = -int(str(x)[1:][::-1])
        return 0 if final_value >= 2**31-1 or final_value <= -2**31 else final_value 

def main():
    testcases = [123, -123, 120, 0]
    for testcase in testcases:
        returnValue = reverse(testcase)
        print(returnValue)
        

if __name__ == "__main__":
    main()