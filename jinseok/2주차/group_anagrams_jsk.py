def group_anagrams(strs):
    anagrams = {}
    for str in strs:
        key = "".join(sorted(str))
        if key not in anagrams:
            anagrams[key] = [str]
        else:
            anagrams[key].append(str)
        
    return anagrams.values()

        
strs = ["eat", "tea", "tan", "ate", "nat","bat"]
print(group_anagrams(strs))
