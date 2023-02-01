# Problem: Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Three approaches:
# 1. Recursion
# 2. BFS
# 3. DFS

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):   # Constructor
        self.val = val  # Value
        self.left = left    # Left child
        self.right = right  # Right child

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

class Solution:
    # Approach: Use recursion to traverse the tree and return the max depth of the left and right subtrees.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxDepthRecursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepthRecursion(root.left), self.maxDepthRecursion(root.right))
    
    
    # Approach: Use BFS to traverse the tree and return the max depth of the tree.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0   # Keep track of the level
        q = deque([root])   # Add the root to the queue

        while q:    # While the queue is not empty

            for i in range(len(q)): # Iterate through the queue
                node = q.popleft()  # Remove the first element from the queue
                if node.left:   # If the node has a left child, add it to the queue
                    q.append(node.left)
                if node.right:  # If the node has a right child, add it to the queue
                    q.append(node.right)

            level += 1  # Increment the level
        return level    # Return the level

    
    # Approach: Use DFS to traverse the tree and return the max depth of the tree.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]] # Add the root to the stack
        result = 0  # Keep track of the max depth

        while stack:    # While the stack is not empty
            node, depth = stack.pop()   # Remove the last element from the stack

            if node:    # If the node is not None
                result = max(result, depth) # Update the max depth
                stack.append([node.left, depth + 1]) # Add the left child to the stack
                stack.append([node.right, depth + 1])   # Add the right child to the stack

        return result   # Return the max depth

        
        
        

                
    
    
    

    
if __name__ == "__main__":
    print("Recursive Solution Depth: ", + Solution().maxDepthRecursion(root))
    print("BFS Solution Depth: ", + Solution().maxDepthBFS(root))
    print("DFS Solution Depth: ", + Solution().maxDepthDFS(root))