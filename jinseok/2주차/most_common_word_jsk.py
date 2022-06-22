import re
def most_common_word(string1, banned):
    string1 = string1.lower()# 소문자 전처리
    string1 = re.sub(r'[^\w]',' ', string1).split() # 단어가 아니면 공백으로 전처리
    # 공백을 기준으로 string1 에 저장
    
    counts = {} # 단어 빈도수 값 저장 dict()
    
    for i in string1: # 단어 개수 만큼 반복
         if i not in banned: # 밴에 있는 값인지 확인
             if i in counts: # 빈도수 확인
                 counts[i] +=1
             else:
                 counts[i] = 1

            
    return max(counts, key= counts.get)# 가장 value가 큰 값중 key 값을 출력



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph,banned))

