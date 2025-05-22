import sys
import json
import os
from datetime import datetime
import cmd

class TaskTracker(cmd.Cmd):
    intro = 'Task Tracker CLI'
    prompt = 'task_cli '
    file = None

    def __init__(self, tasks_file='tasks.json'):
        super().__init__()
        self.tasks_file = tasks_file
        self.tasks =  self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.tasks_file):
            return []

        try:
            with open(self.tasks_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f'Error: The task file ({self.tasks_file}) is corrupted.')
            return []

    def save_tasks(self):
        with open(self.tasks_file, 'w') as file:
            json.dump(self.tasks, file, indent=2)


    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

    def do_exit(self, arg):
        print('Goodbye')
        return True

    def do_quit(self, arg):
        return self.do_exit(arg)
            

if __name__ == '__main__':
    TaskTracker().cmdloop()
