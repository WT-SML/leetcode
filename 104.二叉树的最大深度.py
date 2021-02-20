"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

通过次数348,978提交次数460,741
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass

# ts 解法
# /**
#  * Definition for a binary tree node.
#  * class TreeNode {
#  *     val: number
#  *     left: TreeNode | null
#  *     right: TreeNode | null
#  *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
#  *         this.val = (val===undefined ? 0 : val)
#  *         this.left = (left===undefined ? null : left)
#  *         this.right = (right===undefined ? null : right)
#  *     }
#  * }
#  */
#
# function maxDepth(root: TreeNode | null): number {
#  return root ? Math.max(maxDepth(root!.left), maxDepth(root!.right)) + 1 : 0
# }
