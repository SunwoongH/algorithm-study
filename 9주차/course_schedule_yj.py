import collections
 
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x,y in prerequisites:
            graph[x].append(y)
 
        traced = set()
        visited = set()
 
        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True
            
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
 
            return True
 
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
 
        return True