class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # remember the color of the starting cell (the color we are replacing)
        origin = image[sr][sc]

        # if the start cell already has the new color, nothing to change
        # (also stops an infinite loop)
        if origin == color:
            return image

        # m = number of rows, n = number of columns
        m, n = len(image), len(image[0])

        # this function paints one cell, then spreads to its neighbors
        def dfs(r, c):
            # stop if: off the top/bottom, off the left/right,
            # or this cell is not the original color
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != origin:
                return

            # paint this cell with the new color
            image[r][c] = color

            dfs(r + 1, c)   # go down
            dfs(r - 1, c)   # go up
            dfs(r, c + 1)   # go right
            dfs(r, c - 1)   # go left

        # start spreading from the starting cell
        dfs(sr, sc)

        # return the repainted image
        return image