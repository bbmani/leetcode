def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    returnValue = 0
    for x in jewels: returnValue += stones.count(x)
    return returnValue

def main():
    jewels = "aA"
    stones = "aAAbbbb"
    returnValue = numJewelsInStones(jewels=jewels, stones=stones)
    print(returnValue)
    
if __name__ == "__main__":
    main()