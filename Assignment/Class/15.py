'''Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" 
and "{{{" are invalid. '''

class ParenthesesChecker:
    def __init__(self):
        self.opening = '({['
        self.closing = ')}]'
        self.match = {')': '(', '}': '{', ']': '['}

    def is_valid(self, s):
        stack = []
        for char in s:
            if char in self.opening:
                stack.append(char)
            elif char in self.closing:
                if not stack or stack.pop() != self.match[char]:
                    return False
            else:
                return False
        return not stack

checker = ParenthesesChecker()
print(checker.is_valid("()"))  
print(checker.is_valid("({[)]"))  
print(checker.is_valid("{{{"))  
