class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # We don't actually need to simulate the queue rotating.
        # Students just keep cycling until someone who wants the top sandwich
        # reaches the front, so the ORDER of students doesn't matter.
        # All we need is: how many students want 0s and how many want 1s?

        # Assume everyone is stuck at first, we'll subtract as students eat.
        res = len(students)

        # Count of each preference, e.g. {0: 2, 1: 3}
        cnt = Counter(students)

        # Sandwiches are a stack, so we must handle them in order, top first.
        for s in sandwiches:

            # Is there still a student who wants this sandwich?
            if cnt[s] > 0:
                # Yes: some student will eventually get to the front and eat it.
                # One less hungry student, one less student wanting this type.
                res -= 1
                cnt[s] -= 1

            # No student left wants this type.
            else:
                # The top sandwich is stuck, and we can't skip it because it's a stack.
                # So nobody else can eat either, and everyone still in res is stuck.
                return res

        # We got through every sandwich, so every student ate. res is 0.
        return res