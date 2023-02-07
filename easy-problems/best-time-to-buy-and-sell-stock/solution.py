def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # min_value = prices[0]
        # prices_next = prices[1:]
        # max_value = 0
        # increasing = 0
        # for x in prices_next:
        #     if x < min_value:
        #         min_value = x
        #     elif x > max_value:
        #         max_value = x
        # if max_value == 0:
        #     return 0
        # else:
        #     return max_value-min_value
        min_value = prices[0]
        max_value = 0
        increasing = 0
        final_list = list()
        for i in range(len(prices[1:])):
            if prices[i] < min_value and increasing == 0:
                min_value = prices[i]
            elif prices[i] > max_value:
                max_value = prices[i]
                increasing = 1
            elif prices[i] < max_value and prices[i-1] == max_value:
                increasing = 0
                print(max_value)
                print(min_value)
                final_list.append(max_value-min_value)
        print(max(prices))
        print(type(max(prices)))
                

if __name__ == "__main__":
    prices = [2,4,1]
    maxProfit(prices)