# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false

# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        def isEqual(tree_1, tree_2):
            if not tree_1 and tree_2:
                return False
            if not tree_2 and  tree_1:
                return False
            if not tree_1 and not tree_2:
                return True
            if tree_1.val != tree_2.val:
                return False
            right_equality = isEqual(tree_1.right, tree_2.right)
            left_equality = isEqual(tree_2.left, tree_2.left)
            if right_equality is True and right_equality == left_equality:
                return True
            else:
                return False
        return isEqual(p,q)