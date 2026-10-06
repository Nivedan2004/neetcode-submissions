class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Buckets: count[0] = number of 0s (red)
        #          count[1] = number of 1s (white)
        #          count[2] = number of 2s (blue)
        count = [0, 0, 0]

        # Pass 1: put every number into its bucket (just count it)
        for n in nums:
            count[n] += 1

        # Pass 2: rebuild the array from the buckets, in order 0 -> 1 -> 2
        i = 0  # next position in nums to overwrite
        for color in range(3):              # go bucket by bucket: 0, 1, 2
            for _ in range(count[color]):   # as many times as we counted it
                nums[i] = color             # write the color
                i += 1                      # move to the next position