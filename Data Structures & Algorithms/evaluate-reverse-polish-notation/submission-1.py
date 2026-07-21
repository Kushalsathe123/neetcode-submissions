class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()
                res = 0
                if i == "+":
                    res = a+b
                elif i == "/":
                    res = int(b/a)
                elif i == "*":
                    res = a*b
                else :
                    res = b-a
                
                stack.append(res)
        return int(stack[-1])