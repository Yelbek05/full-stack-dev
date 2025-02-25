import json
import argparse
import os

DATA_FILE = "tasks.json"
parser = argparse.ArgumentParser(description="Task Manager")
parser.add_argument('command', choices=['add', 'list', 'update', 'delete'], help="Choose a command")
parser.add_argument("--task", type=str, help="Task to add")
parser.add_argument('--id', type=int, help="Task ID")

def load_tasks(DATA_FILE):
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            tasks = json.load(file)
            return tasks if isinstance(tasks, list) else []
    except json.JSONDecodeError:
        return []

def add_tasks(args, DATA_FILE):
    tasks = load_tasks(DATA_FILE)

    if args.task:
        new_id = max([task["id"] for task in tasks] or [0]) + 1
        new_task = {"id": new_id, "task": args.task}

        tasks.append(new_task)
        with open(DATA_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"{tasks}\n")
        print("Task was added successfully")
    else:
        print("Error: No task provided.")


def list_tasks(DATA_FILE):
    tasks = load_tasks(DATA_FILE)
    for task in tasks:
        print(f" ID:{task['id']}, {task['task']}")

def main():
    args = parser.parse_args()
    if args.command == "add":
        add_tasks(args, DATA_FILE)
    elif args.command == 'list':
        list_tasks(DATA_FILE)

if __name__ == '__main__':
    main()