class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashSet:
                return [hashSet[diff], i]
            hashSet[n] = i
        return

        