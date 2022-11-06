from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_task = Counter(tasks)
        most_task_count = count_task.most_common(1)[0][1]
        print(most_task_count)
        last = 0
        for task in count_task.items():
            if task[1] == most_task_count:
                last += 1
        return max((most_task_count - 1) * (n + 1) + last, len(tasks))