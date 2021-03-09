class TreeNode:
  def __init__(self,val=0, left = None, right= None):
    self.val = val
    self.right = right
    self.left = left

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
      def check(root):
        if not root:
          return 0 #맨 마지막 노드의 자식만 0 할당

        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left-right)>1: #높이 차이가 1보다 크면 -1 리턴
          return -1

        return max(left,right)+1 # 자식노드보다 1씩 증가됨

      return check(root) != -1



root: TreeNode = [3,9,20,None,None,15,7]

s = Solution()
a = s.isBalanced(root)
print(a)