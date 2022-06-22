
nums =  [-1,0,1,2,-1,-4]

result = []
nums.sort()

for i in range(len(nums)):
  left, right = i + 1, len(nums) -1
  while left < right:
    sum3 = nums[i] + nums[left] + nums[right]
    if sum3 < 0:
      left += 1
    elif sum3>0:
      right -=1
    else:
      temp = [nums[i], nums[left], nums[right]]
      if temp not in result:
        result.append(temp)
      left +=1
      right -=1
print(result)