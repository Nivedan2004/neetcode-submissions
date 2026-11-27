class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # maps each ORIGINAL node -> its COPY
        oldToNew = {}

        # returns the copy of this node (and copies all its neighbors too)
        def dfs(node):
            # already copied this node? reuse the copy, don't make another
            if node in oldToNew:
                return oldToNew[node]

            # make a new node with the same value (no neighbors yet)
            copy = Node(node.val)

            # save it in the dictionary RIGHT AWAY, before the neighbors
            # (so a neighbor that points back to me finds my copy)
            oldToNew[node] = copy

            # for each original neighbor, get its copy and connect it to my copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        # if the graph is empty return None, else start copying from the first node
        return dfs(node) if node else None