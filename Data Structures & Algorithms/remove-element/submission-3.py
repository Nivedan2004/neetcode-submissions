class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # You initialize k at position 0

        for i in range(len(nums)): # i scans every element, one by one
            if nums[i] != val:  # keep this one, it's not the value we want gone
                nums[k] = nums[i] # copy it to the next free spot at the front
                k += 1 # that spot is used now, move k to the next one
        return k # how many elements are not val