from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        char, digit = [], []
        for log in logs:
            if log.split()[1].isdigit:
                digit.append(log)
            else:
                char.append(log)
        digit.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return char + digit