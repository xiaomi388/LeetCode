# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def dfs(pre_beg, pre_end, post_beg, post_end):
            if pre_end == pre_beg:
                return None
            node = TreeNode(pre[pre_beg])
            #print(pre_beg, pre_end, post_beg, post_end)
            i = 0
            for i in range(post_beg, post_end-1):
                if post[i] == pre[pre_beg+1]:
                    break
            else:
                return node
            node.left = dfs(pre_beg+1, pre_beg+i-post_beg+2, post_beg, i+1)
            node.right = dfs(pre_beg+i-post_beg+2, pre_end, i+1, post_end-1)
            return node
        return dfs(0, len(pre), 0, len(post))

