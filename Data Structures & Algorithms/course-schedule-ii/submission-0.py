class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = [[] for i in range(numCourses)]
        #degree[i] means number of prerequisites course [i] still has
        degree= [0] * numCourses
        #[1, 0]  mean 1 degree 1, 0 degree 0
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] +=1
        #Put all courses with no prerequisites first
        queue = [i for i in range(numCourses) if degree[i] == 0]

        for current in queue:
            for next_course in G[current]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    queue.append(next_course)
        #There is a cycle
        if len(queue) != numCourses:
            return []

        return queue