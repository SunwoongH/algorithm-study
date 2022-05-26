#3. 로그파일 재정렬
#letter-logs : 모든 단어는 영문 소문자로 구성
#Digit-logs : 모든 단어는 숫자로 구성

# 아이디어 1. letter logs가 digit logs보다 먼저 앞에 온다. 따라서 숫자와 문자를 구분해야 하므로 split 함수로 공백 엔터 기준으로 나눈다. 
#        2. 문자 숫자를 나누어서 각각 리스트에 저장
#        3. isdigit() ->  숫자인지 판별
#        4.  sort(key=len(변수))로 하여 속성의 길이를 기준으로 오름차순 정렬
#         5.변수.split()[1:]으로 1번부터 그 뒤의 모든 결과를 반환
 


def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits =[], [] 
        for log in logs:
            
            if log.split()[1].isdigit(): #첫번째는 식별자 , 두번째 인덱스는 로그이므로 두번째 인덱스에 해당하는 부분이 숫자인지 문자인지 파악해주기 위해 isdigit 함수 사용
                digits.append(log) 
            else:
                letters.append(log)
        #문자로 구성된 로그들에 대한 정렬을 sort함수를 이용하여 시작
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits