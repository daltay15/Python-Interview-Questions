# Problem: Balanced Binary Tree
# Given the root of a binary tree, determine if it is height-balanced.

from typing import Optional 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):   # Constructor for binary tree node
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):  # Depth first search
            if not root:    # If the root is None,
                return [True, 0]    # Return True and 0

            left, right = dfs(root.left), dfs(root.right)   # Recursively call the function on the left and right child
            balanced = (left[0] and right[0] and    # Check if the left and right child are balanced
                        abs(left[1] - right[1]) <= 1)   # Check if the tree is balanced
            
            return [balanced, 1 + max(left[1], right[1])]   # Return the balanced and the height of the tree
        
        return dfs(root)[0]
    
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().isBalanced(root))