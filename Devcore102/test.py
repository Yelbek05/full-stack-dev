from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = {}  # Example: {1: ("Task description", "2025-01-01")}
    
    def add_task(self, id, description, deadline):
        self.tasks[id] = (description, deadline)
    
    def sort_tasks_by_date(self):
        # Convert tasks to a list and sort by the parsed deadline
        sorted_tasks = sorted(
            self.tasks.items(),
            key=lambda task: datetime.strptime(task[1][1], "%Y-%m-%d")
        )
        # Update self.tasks with the sorted order
        self.tasks = {id: (description, deadline) for id, (description, deadline) in sorted_tasks}
    
    def display_tasks(self):
        for id, (description, deadline) in self.tasks.items():
            print(f"ID: {id}, Description: {description}, Deadline: {deadline}")

# Example usage
manager = TaskManager()
manager.add_task(1, "Complete project", "2025-02-01")
manager.add_task(2, "Submit report", "2025-01-25")
manager.add_task(3, "Prepare presentation", "2025-01-30")

print("Before sorting:")
manager.display_tasks()

manager.sort_tasks_by_date()

print("\nAfter sorting:")
manager.display_tasks()
