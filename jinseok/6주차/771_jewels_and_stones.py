import collections


def numJewelsInStones(S,J):
  freqs = collections.Counter(S)
  count = 0
  
  for char in J:
    count += freqs[char]
    
  return count

a = 'aAAbbbb'
b = 'aA'
print(numJewelsInStones(a,b))