# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []                      # final answer

        q = collections.deque()       # the queue
        q.append(root)                # put the root in it

        while q:                      # repeat until queue is empty
            qLen = len(q)             # how many nodes are in this level
            level = []                # values of this level go here

            for i in range(qLen):     # go through this level's nodes
                node = q.popleft()    # take the first node out

                if node:              # only if it's a real node
                    level.append(node.val)   # save its value
                    q.append(node.left)      # add left child to queue
                    q.append(node.right)     # add right child to queue

            if level:                 # if this level has values
                res.append(level)     # add it to the answer

        return res                    # done