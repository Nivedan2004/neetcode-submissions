class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty grid means no islands
        if not grid:
            return 0

        # rows, cols = size of the grid (never changes)
        rows, cols = len(grid), len(grid[0])

        # remembers every land cell we have already seen
        visit = set()

        # counts the islands
        islands = 0

        # marks one whole island as visited, starting from cell (r, c)
        def bfs(r, c):
            q = collections.deque()   # line of cells waiting to be checked
            visit.add((r, c))         # mark the start cell as seen
            q.append((r, c))          # put the start cell in line

            # keep going while cells are waiting in line
            while q:
                # take the first cell out: this is where I am right now
                row, col = q.popleft()

                # the 4 moves: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # position of the neighbor I am checking
                    r, c = row + dr, col + dc

                    # go to the neighbor only if:
                    # inside the grid, it is land, and I haven't seen it before
                    if (r in range(rows) and c in range(cols)
                            and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))    # check its neighbors later
                        visit.add((r, c))   # mark as seen right now

        # look at every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # land that we haven't seen = a brand new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)       # mark the whole island as seen
                    islands += 1    # count it once

        # total number of islands
        return islands