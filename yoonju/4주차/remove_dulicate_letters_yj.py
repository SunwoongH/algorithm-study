import collections

def removeDuplicateLetters(self, s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
    
        while stack and counter[stack[-1]] > 0 and char < stack[-1]:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)