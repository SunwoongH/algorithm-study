def reorder_logfiles(logs):
  letters, digits = [],[] # 문자, 숫자 저장 배열 생성
  for log in logs: 
    if log.split()[1].isdigit(): # 공백을 기준으로 숫자인지 판별
      digits.append(log) # 숫자는 digits에
    else:
      letters.append(log) # 문자는 letters에
      
  letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 식별자를 제외한 index 1값을 비교 만약 같으면 식별자 index 0으로 비교
  return letters + digits # letters 와 digits를 더해서 return

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]

print(reorder_logfiles(logs))