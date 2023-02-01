# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:  
        stack = []  # Create a stack
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # Dictionary to map closing parentheses to opening parentheses

        for c in s: # Iterate through the string
            if c in closeToOpen: # If closing parentheses
                if stack and stack[-1] == closeToOpen[c]:   # If stack not empty and value at top of stack is matching opening parentheses 
                    stack.pop() # Pop the top of the stack
                else:   # If stack is empty or value at top of stack is not matching opening parentheses
                    return False    # Return false
            else:   # If open parentheses
                stack.append(c) # If open parentheses append to stack and keep iterating

        return True if not stack else False # return True if stack is empty else false


if __name__ == "__main__":
    s = "()[]{}"
    print(Solution().isValid(s))