
# 이해 못함 ㅠㅠ
import collections

def course(num, list_k):
  graph = collections.defaultdict(list)
  
  for x, y  in list_k:
    graph[x].append(y)
    
  traced = set()
  
  def dfs(i):
    
    if i in traced:
      return False
    
    traced.add(i)
    
    for y in graph[i]:
      if not dfs(y):
        return False
      
    traced.remove(i)
    
    return True
  
  for x in list(graph):
    if not dfs(x):
      return False
    
  return True

print(course(2, [[1,0]]))
print(course(2, [[1,0],[0,1]]))
