def reorderLogFiles(logs: list[str]):

    letters, digits = [], []

    #입력 받은 리스트에 대하여 숫자 문자 판별
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #문자가 동일할 경우 식별자 순으로 정렬하기 위한 코드
    ## 람다 표현식으로 먼저 문자를 검색 후 index 1에 해당하는 문자가 동일할 시, index 0 번째를 비교하여 sort한다.
    letters.sort(key=lambda letters: (letters.split()[1], letters.split()))
    
    print(list(letters+digits))

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]
reorderLogFiles(logs)