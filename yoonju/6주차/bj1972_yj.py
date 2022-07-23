import sys

while True:
  word = sys.stdin.readline().strip()
  if word == '*':
    break

  for interval in range(len(word)-1):
    used = []
    state = False

    for j in range(len(word)-1-interval):
      pair = [word[j], word[j+interval+1]]

      if pair in used:
        state = True
        print('%s is NOT surprising' %word)
        break

      else:
        used.append(pair)

    if state:
      break
  
  if state:
    continue
    
  else:
    print('%s is surprising.' %word)