import sys
import json
import os
import datetime
import cmd

class TaskTracker(cmd.Cmd):
    into = 'Task Tracker CLI'
    prompt = 'track_cli '
    file = None

    def __init__(self, tasks_file='tasks.json'):
        super().__init__()
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()


    def load_tasks(self):
        """Function to load taks from the saved json file and it also
        create file if it if does not exist
        """
        if not os.path.exists(self.tasks_file):
            return []

        try:
            with open(self.tasks_file, 'r') as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.load(content)
        except json.JSONDecodeError as e:
            print(f'Error: Invalid JSON format in {TASK_FILE}.{str(e)}')
            return []

    def save_tasks(self):
        """save task to json file """
        try:
            with open(self.tasks_file, 'w') as file:
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f'Error saving tasks: {str(e)}')
            return []


    def tasks_id(self):
        """Generate the task ID for the task"""
        if not self.tasks:
            return 1
        return max(self.task['id'] for task in self.tasks) + 1


    def get_current_timestamp(self):
        """Generate current timestamp in ISO format"""
        return datetime.datetime.now().isoformat()


    def find_task_by_id(self, task_id):
        """Find task by its ID"""
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                return task, index
            return None, -1


    def validate_task_id(self, task_id_str):
        """Validate and convert task ID to integer"""
        try:
            task_id = int(task_id_str)
            if task_id <= 0:
                print('Error: Task ID must be a positive integer')
                return None
            return task_id
        except ValueError:
            print('Error: Task ID must be a valid integer')
            return None


    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

    def do_exit(self, arg):
        print('Goodbye')
        return True

    def do_quit(self, arg):
        return self.do_exit(arg)


if __name__ == '__main__':
    TaskTracker().cmdloop()
