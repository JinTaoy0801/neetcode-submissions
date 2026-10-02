from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        zero = [0] * numCourses
        hm = {i:[] for i in range(numCourses)}
        ret = []
        for i in range(len(prerequisites)):
            zero[prerequisites[i][0]]+=1
            hm[prerequisites[i][1]].append(prerequisites[i][0])


        queue = deque()

        for i in range(len(zero)):
            if zero[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            ret.append(course)
            preq = hm[course]
            for p in preq:
                zero[p]-=1
                if zero[p]==0:
                    queue.append(p)
                
        for course in zero:
            if course > 0:
                return []
            
        return ret
                


        



        