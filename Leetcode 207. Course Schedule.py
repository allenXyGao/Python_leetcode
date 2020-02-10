# Leetcode 207. Course Schedule
'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

'''

# Topological sort via BFS

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # specify the label of all courses
        courses_id = [i for i in range(numCourses)]
        # initiate the indegree of all courses
        indegree = {u:0 for u in courses_id}
        course_dict = {u:[] for u in courses_id}
        for u, v in prerequisites:
            indegree[u] += 1
            course_dict[v].append(u) # append的都是v的后续课程
        # first course
        Q = [u for u in courses_id if indegree[u] == 0]
        
        # BFS
        s = []
        while Q:
            node = Q.pop()
            s.append(node)
            for ele in course_dict[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    Q.append(ele)
        return len(s) == numCourses
            