import heapq
from task import Task

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add_task(self,task_name, priority):
        task = Task(task_name, priority)
        heapq.heappush(self.heap, task)

    def process_task(self):
        if len(self.heap) != 0:
           return heapq.heappop(self.heap)
        else: 
            return None

    def peek_next_task(self):
        if len(self.heap) != 0:
            return self.heap[0]
        else:
            return None

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False