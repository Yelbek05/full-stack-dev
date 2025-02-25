import argparse
import json
import os

DATA_FILE = "tasks.json"
parser = argparse.ArgumentParser(description="Task Manager")
parser.add_argument('command', choices=['add', 'list', 'update', 'delete'], help="Choose a command")
parser.add_argument('--task', type=str, help="Task to add")
parser.add_argument('--id', type=int, help="Task ID")
def load_tasks(DATA_FILE):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                tasks = json.load(file)
                if not isinstance(tasks, list):  # Ensure it's a list
                    return []
                return tasks
            except json.JSONDecodeError:  # Handle empty or corrupt JSON
                return []
    return []  # Return an empty list if file does not exist


def add_tasks(args, DATA_FILE):
    tasks = load_tasks(DATA_FILE)

    if args.task:
        new_id = max([task["id"] for task in tasks], default=0) + 1
        new_task = {"id": new_id, "task": args.task}

        tasks.append(new_task)
        with open(DATA_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"{tasks}\n")
    else:
        print("Error: No task provided.")

    # Ensure tasks.json is initialized if missing
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

def list_tasks(DATA_FILE):
    tasks = load_tasks(DATA_FILE)
    for task in tasks:
        print(f"{task['id']}: {task['task']}")

# def update_tasks():

def delete_tasks(DATA_FILE, args):
    tasks = load_tasks(DATA_FILE)
    if args.id is None:
        print("Please enter the ID of the task to delete")
    for task in tasks:
        print(f"{task['id']}: {task['task']}")
    
    updated_task = [task for task in tasks if task['id'] != args.id]

    if len(updated_task) == len(tasks):
        print(f"There is no task with ID {args.id}")
    else:
        with open(DATA_FILE, "w") as file:
            json.dump(updated_task, file, indent=4)
        print(f"Task with ID {args.id} deleted, to see the update please run list command")



def main():
    args = parser.parse_args()

    if args.command == "add": 
        add_tasks(args, DATA_FILE)
    elif args.command == "list":
        list_tasks(DATA_FILE)
    elif args.command == "delete":
        delete_tasks(DATA_FILE, args)
    else:
        print("Not impelemented yet")
if __name__ == "__main__":
    main()