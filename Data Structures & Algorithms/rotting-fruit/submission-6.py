class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # line of rotten fruits whose neighbors we still need to rot
        q = deque()

        # time = minutes passed, fresh = how many fresh fruits are left
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        # scan the grid once
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:        # fresh fruit: count it
                    fresh += 1
                if grid[r][c] == 2:        # rotten fruit: put it in line
                    q.append([r, c])

        # the 4 moves: right, down, left, up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # keep going while rotten fruits can spread AND fresh fruits remain
        while q and fresh > 0:

            # handle only the fruits that are rotten right now (= one minute)
            for i in range(len(q)):
                r, c = q.popleft()          # take one rotten fruit out

                for dr, dc in directions:   # look at its 4 neighbors
                    row, col = dr + r, dc + c

                    # skip if off the grid, or not fresh (empty or already rotten)
                    if (row < 0 or row == len(grid) or col < 0
                            or col == len(grid[0]) or grid[row][col] != 1):
                        continue

                    grid[row][col] = 2      # fresh fruit rots (also acts as "visited")
                    q.append([row, col])    # it will spread next minute
                    fresh -= 1              # one less fresh fruit

            time += 1                       # this whole layer = one minute passed

        # all fresh fruit rotted -> return minutes, otherwise some was unreachable
        return time if fresh == 0 else -1