def solution_reverse(s):
    small = []
    for char in s:
      if char.isalnum():
        small.append(char.lower())

    if small == small[::-1]:
      return True
    else:
      return False

answer = solution_reverse("A man, a plan, a canal: Panama")
if answer: print("회문입니다")
else: print("회문이 아닙니다")