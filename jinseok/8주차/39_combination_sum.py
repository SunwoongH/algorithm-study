#조합의 합

def combinationSum(candidates,target):
  
  def combination(num):
    
    if sum(temp) == target:
      
      results.append(temp[:])
      
    elif sum(temp) < target:
      
      for i in range(num, len(candidates)):
        
        temp.append(candidates[i])
        combination(i)
        
        temp.pop()  # 다른 조합의 요소를 집어 넣기 위해
  results = []
  temp = []
  combination(0)
  return results


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))