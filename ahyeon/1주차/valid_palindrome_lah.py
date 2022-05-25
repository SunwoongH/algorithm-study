#1. Palindrome Algorithm 유효한 팰린드롬 판별하기
# 팰린드롬 : 거꾸로 읽어도 제대로 읽히는 것 ex) 스위스 , 토마토
# 아이디어 1. 입력받은 문자열의 특수문자 및 공백, 대문자-> 소문자로 변경한다.  
#        2. 역순으로 뒤집기
#        3. 문자열과 같은지를 비교하여 True , False 리턴하기 
# 

from curses.ascii import isalnum

string = input()

#replace 함수로 공백제거하기
string = string.replace(" ", "")

#isalnum 함수로 문자가 영숫자인 경우인지 확인하고 특수문자를 제거한다. 
string =  "".join(char for char in string if char.isalnum())

#대문자 소문자로 변경하기 
string = string.lower()

#역순으로 뒤집기 -> 문자열 슬라이싱 사용 [::-1] 뒤에서부터 잘라서 문자열 출력
result = string[::-1]

#문자열이 같은지를 비교하여 True , False 리턴하기 
if string == result:
    print("True")
else:
    print("False")

