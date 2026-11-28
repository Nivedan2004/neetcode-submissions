class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course -> list of courses I must take BEFORE it
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # courses on the CURRENT path only (the loop detector)
        visitSet = set()

        # can I finish this course (and everything it needs)?
        def dfs(crs):
            # already on my current path -> I walked in a circle -> impossible
            if crs in visitSet:
                return False

            # no prerequisites left -> nothing blocks me -> fine
            if preMap[crs] == []:
                return True

            # enter this course: put it on the current path
            visitSet.add(crs)

            # every prerequisite must also be finishable
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # done with this course: take it off the current path
            visitSet.remove(crs)

            # proven safe: clear its list so we never re-check it
            preMap[crs] = []
            return True

        # start from every course (they may not all be connected)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True