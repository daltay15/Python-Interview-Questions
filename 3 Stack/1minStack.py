# Description: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Approach: Use 2 stacks, one for storing the elements and other for storing the min element at each point of time
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for n elements in stack

input = ["MinStack","push","push","push","getMin","pop","top","getMin"] 
input = [[],[-2],[0],[-3],[],[],[],[]]


class MinStack: # MinStack class
    
    def __init__(self): # Constructor
        self.stack = [] # Stack to store elements
        self.minStack = []  # Stack to store min element at each point of time
        
    def push(self, val: int) -> None:   # Push element to stack
        self.stack.append(val)  # Append element to stack
        val = min(val, self.minStack[-1] if self.minStack else val) # Take min of val and top of minStack if ! empty else take val
        self.minStack.append(val)   # Append min to minStack

    def pop(self) -> None:  # Pop element from stack
        self.stack.pop()    # Pop element from stack
        self.minStack.pop() # Pop element from minStack
        
    def top(self) -> int:   # Get top element of stack
        return self.stack[-1]   # Return top element of stack

    def getMin(self) -> int:    # Get min element of stack
        return self.minStack[-1]    # Return top element of minStack
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()