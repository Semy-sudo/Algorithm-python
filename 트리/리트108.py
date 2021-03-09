# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      if not nums:# 배열안에 값이 없으면
        return None
      
      mid = len(nums)//2 #딱 중간값
      node = TreeNode(nums[mid])
      node.left = self.sortedArrayToBST(nums[:mid])
      node.right = self.sortedArrayToBST(nums[mid+1:])

      return node

s = Solution()
nums = [-10,-3,0,5,9]
s.sortedArrayToBST(nums)
