from typing import List
import collections
import re

def mostCommonWord(paragaph : str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragaph)    
    .lower().split() if word not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
mostWord = mostCommonWord(paragraph, banned)

print(mostWord)