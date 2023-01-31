# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

s = "()[]{}"



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
        # if stack not empty and value at top of stack is matching opening parentheses.
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop() # Pop the top of the stack
                else:
                    return False
            else:
                stack.append(c) # If open parentheses append to stack and keep iterating

        return True if not stack else False # return True if stack is empty else false


if __name__ == "__main__":
    print(Solution().isValid(s))