class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # N = size of the grid (it's N x N, so rows = cols = N)
        N = len(grid)

        # the line of cells waiting to be visited
        # each item is (row, col, length), length = how many cells on the path so far
        # we start at the top-left (0, 0) and the start cell counts as 1
        q = deque([(0, 0, 1)])

        # cells we have already added to the line, so we never add one twice
        # (note: {(0, 0)} is the cleaner way to write this, but yours passed)
        visit = set((0, 0))

        # the 8 moves: right, down, left, up, then the 4 diagonals
        # each is [row change, column change]
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        # keep going while cells are waiting in line
        while q:
            # take the first cell out of the line
            # r, c = where I am, length = path length to get here
            r, c, length = q.popleft()

            # skip this cell if:
            #   min(r, c) < 0   -> I walked off the top or left edge
            #   max(r, c) >= N  -> I walked off the bottom or right edge
            #   grid[r][c]      -> the cell is 1 (blocked), since 1 counts as True
            # "continue" = skip this cell, go take the next one from the line
            if (min(r, c) < 0 or max(r, c) >= N or grid[r][c]):
                continue

            # am I at the bottom-right cell (the goal)?
            # BFS reaches it first by the shortest path, so return the length
            if r == N - 1 and c == N - 1:
                return length

            # look at all 8 neighbors
            for dr, dc in direct:
                # if I haven't added this neighbor before
                if (r + dr, c + dc) not in visit:
                    # add it to the line, with one more cell on the path
                    q.append((r + dr, c + dc, length + 1))
                    # mark it as seen right now so it can't be added twice
                    visit.add((r + dr, c + dc))

        # the line is empty and we never reached the goal: no path exists
        return -1
        