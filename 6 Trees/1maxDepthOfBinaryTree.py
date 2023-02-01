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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        
        level = 0
        q = deque([root])

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level

    
    # Approach: Use DFS to traverse the tree and return the max depth of the tree.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1]) # Add left child to stack
                stack.append([node.right, depth + 1]) # Add right child to stack

        return result

        
        
        

                
    
    
    

    
if __name__ == "__main__":
    print("Recursive Solution Depth: ", + Solution().maxDepthRecursion(root))
    print("BFS Solution Depth: ", + Solution().maxDepthBFS(root))
    print("DFS Solution Depth: ", + Solution().maxDepthDFS(root))