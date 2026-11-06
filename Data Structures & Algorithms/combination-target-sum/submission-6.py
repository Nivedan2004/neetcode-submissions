class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # TAKE the number
            cur.append(nums[i])  # add nums[i] to my group
            dfs(i, cur, total + nums[i]) # try again from the SAME number (reuse allowed), total goes up

            # SKIP the number
            cur.pop()  # remove it from my group (undo the append above)
            dfs(i + 1, cur, total) # move to the NEXT number, total stays the same
        dfs(0, [], 0)  # start: look at the 1st number (i = 0), empty group ([]), total is 0
        return res
        