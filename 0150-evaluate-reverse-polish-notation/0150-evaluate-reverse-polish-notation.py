class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def operator_func(operator, num1, num2):
            num1, num2 = int(num1), int(num2)
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                # Use integer division and handle rounding toward zero
                if num1 * num2 < 0 and num1 % num2 != 0:
                    return num1 // num2 + 1
                else:
                    return num1 // num2


        # # Pop the last element to process
        # char = tokens.pop()
        
        # # Check if `char` is a number (including negative numbers)
        # if char.isdigit() or (char[0] == '-' and char[1:].isdigit()):
        #     return int(char)
        # else:
        #     # Recursive case: `char` is an operator
        #     # Evaluate the right and left operands in correct order
        #     right = self.evalRPN(tokens)
        #     left = self.evalRPN(tokens)
        #     return operator_func(char, left, right)

        stack=[]
        for i,char in enumerate(tokens):
            if char.isdigit() or (char[0] == '-' and char[1:].isdigit()):
                stack.append(char)
            else:
                right=stack.pop()
                left=stack.pop()
                stack.append(operator_func(char, left,right))
            
        return int(stack.pop())