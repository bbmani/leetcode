class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        custom_stack = list()

        for value in tokens:
            match value:
                case "+":
                    top = custom_stack.pop() if custom_stack else 0
                    bottom = custom_stack.pop() if custom_stack else 0
                    custom_stack.append(bottom + top)
                case "-":
                    top = custom_stack.pop() if custom_stack else 0
                    bottom = custom_stack.pop() if custom_stack else 0
                    custom_stack.append(bottom - top)
                case "*":
                    top = custom_stack.pop() if custom_stack else 0
                    bottom = custom_stack.pop() if custom_stack else 0
                    custom_stack.append(bottom * top)
                case "/":
                    top = custom_stack.pop() if custom_stack else 0
                    bottom = custom_stack.pop() if custom_stack else 0
                    custom_stack.append(int(bottom/top))
                case default:
                    custom_stack.append(int(value))
                    

        return int(custom_stack[0])               
        