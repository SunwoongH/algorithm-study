from typing import List
import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = collections.defaultdict(int)
        for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if word not in banned:
                words[word] += 1
        return max(words.items(), key=lambda x: x[1])[0]