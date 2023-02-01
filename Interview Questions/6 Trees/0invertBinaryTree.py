# Problem: Invert a binary tree.
# Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):   # Constructor
        self.val = val  # Value
        self.left = left   # Left child
        self.right = right  # Right child
    
    def __str__(self):  # For printing
        return str(self.val) + " -> "  + str(self.left) + " -> " + str(self.right) # Inorder traversal
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:   
        if not root:    # If the root is None,
            return None 

        # Swap the children
        temp = root.left    # Store the left child in a temp variable
        root.left = root.right  # Set the left child to the right child
        root.right = temp   # Set the right child to the temp variable

        self.invertTree(root.left)  # Recursively call the function on the left child
        self.invertTree(root.right) # Recursively call the function on the right child

        return root # Return the root
    
    
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(Solution().invertTree(root))
    