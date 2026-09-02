class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # making a dict of {courseNum(int): prereqs(list)}
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set() # set of courses on this dfs path

        def dfs(crs): # do a dfs down the graph, way to detect a cycle
            
            if crs in visiting: # means we already saw this -> cycle
                return False
            if preMap[crs] == []: # means that this course has no prereqs
                return True


            # no cycle AND course has no prereqs
            visiting.add(crs) 
            for pre in preMap[crs]:
                if not dfs(pre): # if any of this course's prereqs has a cycle
                    return False
                
            # means that we are done exploring this course path
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True