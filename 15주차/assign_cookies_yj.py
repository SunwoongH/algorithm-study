def findContentChildren(self, g, s):
  g.sort()
  s.sort()

  child=0
  count=0

  for i in range(len(s)):
    if child > len(g)-1:
      return count
      
    if g[child] <= s[i]:
      count+=1
      child+=1
    i+=1
        
  return count