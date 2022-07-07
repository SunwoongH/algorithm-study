class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for char in s:
            if char in '({[':
                temp.append(char)
            else:
                if not temp:
                    return False
                value = temp.pop()
                if value == '(' and char == ')' or value == '{' and char == '}' or \
                    value == '[' and char == ']':
                        continue
                else:
                    return False
        return True if not temp else False