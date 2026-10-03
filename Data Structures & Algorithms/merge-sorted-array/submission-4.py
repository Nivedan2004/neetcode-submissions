class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 has m real numbers, then n empty slots (zeros) at the end.
        # If we merge from the FRONT, we'd overwrite numbers we still need.
        # So we merge from the BACK, where the empty space is, and place the
        # biggest numbers first.

        # last = the position in nums1 we're going to fill next (start at the very end)
        last = m + n - 1

        # m and n are our pointers: they point to the end of the real numbers
        # in each array. Keep going while both arrays still have numbers.
        while m > 0 and n > 0:

            # Compare the biggest remaining number in each array
            if nums1[m - 1] > nums2[n - 1]:
                # nums1's number is bigger, so it goes at the back
                nums1[last] = nums1[m - 1]
                m -= 1  # that number is used, move the pointer left
            else:
                # nums2's number is bigger (or equal), so it goes at the back
                nums1[last] = nums2[n - 1]
                n -= 1  # that number is used, move the pointer left

            # We filled one slot, so move to the next empty slot on the left
            last -= 1

        # If nums2 still has numbers left, they're the smallest ones.
        # Copy them to the front of nums1.
        # (If nums1 has leftovers instead, they're already in the right place,
        # so we don't need to do anything.)
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
            