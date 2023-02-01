# Problem: Diameter of Binary Tree
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Approach: Use recursion to traverse the tree and return the max depth of the left and right subtrees.
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):   # Constructor
        self.val = val  # Value
        self.left = left    # Left child
        self.right = right  # Right child
    
        

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        result = [0]    # Keep track of the max diameter

        def dfs(root):  # Helper function to traverse the tree
            if not root:    # If the root is None, return -1
                return -1   # -1 because we are adding 1 to it later
            
            left = dfs(root.left)   # Get the max depth of the left subtree
            right = dfs(root.right) # Get the max depth of the right subtree

            result[0] = max(result[0], 2 + left + right)    # Update the max diameter

            return 1 + max(left, right) # Return the max depth of the left and right subtrees
        
        dfs(root)   # Call the helper function
        return result[0]    # Return the max diameter

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    print("The diameter of the binary tree is: ", Solution().diameterOfBinaryTree(root))