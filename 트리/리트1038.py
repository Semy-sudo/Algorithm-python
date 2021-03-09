# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #중위순회로 돈다
        if root:
            self.bstToGst(root.right) 
            self.val += root.val #지금까지 누적된 값
            root.val = self.val #현재 노드의 값
            self.bstToGst(root.left)
            
        return root