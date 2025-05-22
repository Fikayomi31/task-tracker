import sys
import json
import os
from datetime import datetime

# json file t save the file
tasks_file = 'tasks.json'


def load_tasks():
    if not os.path.exists(tasks_file):
	return []
    with open(tasks_file, 'r') as f:
        return json.load(f)

def save tasks(tasks):
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=2)

def generate_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def find_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
        return None

def add_task(description):
    tasks = load_tasks()
    task = {
        'id': generate_id(tasks),
        'description': decription,
        'status': 'todo',
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    task.append(task)
    save_task(tasks)

    print(f'Task add successfully (ID: {task['id']})')


def main():
    #if len(sys.argv) < 2:
	#show_usage()
	#return
    try:
	if command == 'add':
	    description = sys.argv[2]
	    add_task(description)
	else:
	    return 

    except (IndexError, ValueError):
	print()

if __name__ ==	'__main__':
    main()
