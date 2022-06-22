
def longest_palindromic_substring(str_1):

    if str_1 == '' or str_1 == len(str_1) * str_1[0]:
        return str_1
    
    p = str_1[0]
    l = 1

    for i in range(len(str_1)):
        for j in range(len(str_1), 0, -1):
            w = str_1[i:j]

            if w == w[::-1] and len(w) >1:
                p = w
                l = len(w)
    return p
str_1 = input()
print(longest_palindromic_substring(str_1))