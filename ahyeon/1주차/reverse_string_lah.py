#2. 문자열 뒤집기
# 아이디어 1. for 루프를 이용하여 입력한 문자열을 배열로 저장 
#        2. 문자열 슬라이싱  [::-1] 이용하여 뒤집어서 출력

from unittest import result


str = input()
#입력받은 문자열 배열로 저장하기
lst=[]
 
 #for 루프를 돌면서 각 문자를 빈 배열에 저장한다. 
for i in str:
     lst.append(i)
     
#[::-1]은 전체 문자열을 뒤로 1개씩 가면서 추출하라는 의미로 문자열을 뒤집는 것과 같은 의미를 가진다. 
result = lst[::-1]

print(result)