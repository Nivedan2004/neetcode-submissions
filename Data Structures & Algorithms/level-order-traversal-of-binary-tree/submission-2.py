# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # final answer: a list of rows
        res = []

        # the line of nodes waiting to be visited
        q = collections.deque()
        q.append(root)  # start with the root in line

        # keep going while someone is still in line
        while q:
            # everyone in line right now is from the SAME row
            # count them so we only handle this row
            qLen = len(q)

            # empty page to write this row's values on
            level = []

            # visit exactly qLen people (this row only)
            for i in range(qLen):
                # take the first person out of the line
                node = q.popleft()

                # skip if it's "nobody" (an empty spot)
                if node:
                    # write this node's VALUE on this row's page
                    level.append(node.val)

                    # put its kids at the BACK of the line
                    # (they're the next row, left first then right)
                    q.append(node.left)
                    q.append(node.right)

            # row is done: save the page (skip it if it's empty)
            if level:
                res.append(level)

        # all rows done
        return res
