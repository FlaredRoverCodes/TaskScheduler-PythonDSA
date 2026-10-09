from priority_queue import PriorityQueue
        
pq = PriorityQueue()
pq.add_task("Fix critical bug", 1)
pq.add_task("Write documentation", 3)
pq.add_task("Update website", 2)
print("Next Task:", pq.peek_next_task().task_name) # Output: Fix critical bug
print("Processing Task:", pq.process_task().task_name) # Output: Fix critical bug
print("Processing Task:", pq.process_task().task_name) # Output: Update website
print("Processing Task:", pq.process_task().task_name) # Output: Write documentation
print("Is Queue Empty:", pq.is_empty()) # Output: True