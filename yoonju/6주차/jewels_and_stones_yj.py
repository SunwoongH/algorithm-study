def numJewelsInstones(self, J, S):
  num = {}
  count = 0

  for char in S:
    if char not in num:
      num[char] = 1
    else:
      num[char] += 1

  for char in J:
    if char in num:
      count += num[char]

  return count