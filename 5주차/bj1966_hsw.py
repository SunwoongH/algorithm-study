import sys
import collections

test = int(sys.stdin.readline())
for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    input_sequence = list(map(int, sys.stdin.readline().split()))
    priority = sorted(input_sequence)
    sequence = collections.deque(zip(input_sequence, range(len(input_sequence))))
    pivot = priority.pop()
    print_count = 1
    while sequence:
        item, index = sequence.popleft()
        if item == pivot:
            if index == m:
                print(print_count)
                break
            print_count += 1
            pivot = priority.pop()
        else:
            sequence.append((item, index))