import re
def pretreatment(): # 문자열 전처리
  str_1 = input()
  str_1 = str_1.lower() # 소문자 변환
  str_1 = re.sub('[^a-z0-9]', '', str_1) # 문자나 숫자를 제외하고는 모두 제거
  return str_1== str_1[::-1] # str_1를 reverse한 값과 비교 boolean 값 return


print(pretreatment())
