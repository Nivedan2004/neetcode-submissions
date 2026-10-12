class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We are searching for the answer: Koko's eating speed (k).
        # Slowest possible speed = 1 banana per hour.
        # Fastest we would ever need = size of the biggest pile
        # (at that speed, every pile takes just 1 hour).
        l, r = 1, max(piles)

        # Start by assuming the fastest speed is our answer.
        # We'll replace it if we find something slower that still works.
        res = r

        # Keep guessing until our search range is empty.
        while l <= r:

            # Guess the speed in the middle of the range.
            k = (l + r) // 2

            # Count how many hours Koko needs at this speed.
            hours = 0
            for p in piles:
                # Each pile takes (pile size / speed) hours, rounded UP.
                # Example: 7 bananas at speed 3 -> 7/3 = 2.33 -> 3 hours.
                # (Koko can't switch piles mid-hour, so partial hours count as full.)
                hours += math.ceil(p / k)

            if hours <= h:
                # Speed k is fast enough to finish in time. 
                # Save it as a possible answer.
                res = min(res, k)

                # But we want the SLOWEST speed that works,
                # so look at slower speeds (left half).
                r = k - 1
            else:
                # Speed k is too slow, Koko runs out of time.
                # So look at faster speeds (right half).
                l = k + 1

        # After the search ends, res holds the slowest speed that works.
        return res

        