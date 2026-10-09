class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority

    def __lt__(self, other):
      return self.priority < other.priority
