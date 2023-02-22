def customSquareFunction(x):
    return x*x

def sortedSquares(nums):
    return sorted(list(map(customSquareFunction, nums)))

def main():
    testcases = [[-4,-1,0,3,10], [-7,-3,2,3,11]]
    for testcase in testcases:
        print(sortedSquares(testcase))

if __name__ == "__main__":
    main()