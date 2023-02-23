class Solution:
    def dailyTemperatures(self, temperatures):
        custom_stack = []
        res = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while custom_stack and temp > custom_stack[-1][1]:
                custom_stack_index, custom_stack_temperature = custom_stack.pop()
                res[custom_stack_index] = index - custom_stack_index

            custom_stack.append((index, temp))

        return res