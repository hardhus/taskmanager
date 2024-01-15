import os
import json
from dataclasses import dataclass, asdict, field
from typing import List, Optional

@dataclass
class Task:
    name: str
    subtasks: List["Task"] = None
    def __post_init__(self):
        if self.subtasks is not None:
            self.subtasks = [Task(**subtask) if isinstance(subtask, dict) else subtask for subtask in self.subtasks]
            # self.subtasks = [Task(subtask.name, subtask.subtasks) for subtask in self.subtasks]

class TaskManager:
    """
    TaskManager class for managing tasks.

    Before using any methods of this class, be sure to call the `Ready` method to initialize the necessary configurations.

    Usage:
    ```
    TaskManager.Ready()
    tasks = TaskManager.loadTasks()
    TaskManager.addTask("Sample Task")
    ```
    """
    UNREADYERR = "Before using any methods of this class, be sure to call the `Ready` method to initialize the necessary configurations."

    @classmethod
    def Ready(cls):
        cls.path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "tasks.json")
        print(cls.path)

    @classmethod
    def loadTasks(cls):
        try:
            cls.path
        except AttributeError as e:
            err = cls.UNREADYERR
            print(err)
            return (err, None)
        if not os.path.exists(cls.path):
            with open(cls.path, "w") as file:
                json.dump(obj={},  fp=file)
        try:
            with open(cls.path, "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError as e:
            print("ŞEYMA NEREDE?")
            with open(cls.path, "w") as file:
                json.dump(obj={},  fp=file)
            tasks = {}
        except Exception as e: 
            print(e)
            tasks = {}
        return (None, tasks)

    @classmethod
    def addTask(cls, taskName: str):
        try:
            cls.path
        except AttributeError as e:
            err = cls.UNREADYERR
            print(err)
            return (err, None)
        err, tasks = cls.loadTasks()
        if err is not None:
            print(err)
        if taskName == "":
            err = "TASK NAME (ŞEYMA) NEREDE?"
            print(err)
            return (err, None)
        elif taskName in tasks.keys():
            err = "task name zaten var."
            print(err)
            return (err, None)
        else:
            tasks[taskName] = {}
            cls.saveTasks(tasks)

    @classmethod
    def saveTasks(cls, tasks):
        try:
            cls.path
        except AttributeError as e:
            err = cls.UNREADYERR
            print(err)
            return (err, None)
        with open(cls.path, "w") as file:
            json.dump(tasks, file)

def print_task(task, level=0):
        indentation = "    " * level
        print(f"{indentation}{task.name}:")
        
        if task.subtasks:
            for subtask in task.subtasks:
                if isinstance(subtask, Task):
                    print_task(subtask, level + 1)
                else:
                    print(f"{indentation}    {subtask}")

if __name__ == "__main__":
    # TaskManager.Ready()
    # TaskManager.addTask("deneme2")
    # print(TaskManager.loadTasks()[1])
    # 4
    subtask1111 = Task("subtask1111")
    subtask1112 = Task("subtask1112")
    subtask1121 = Task("subtask1121")
    subtask1122 = Task("subtask1122")
    subtask1211 = Task("subtask1211")
    subtask1212 = Task("subtask1212")
    subtask1221 = Task("subtask1221")
    subtask1222 = Task("subtask1222")
    subtask2111 = Task("subtask2111")
    subtask2112 = Task("subtask2112")
    subtask2121 = Task("subtask2121")
    subtask2122 = Task("subtask2122")
    subtask2211 = Task("subtask2211")
    subtask2212 = Task("subtask2212")
    subtask2221 = Task("subtask2221")
    subtask2222 = Task("subtask2222")

    # 3
    subtask111 = Task("subtask111", subtasks=[subtask1111, subtask1112])
    subtask112 = Task("subtask112", subtasks=[subtask1121, subtask1122])
    subtask121 = Task("subtask121", subtasks=[subtask1211, subtask1212])
    subtask122 = Task("subtask122", subtasks=[subtask1221, subtask1222])
    subtask211 = Task("subtask211", subtasks=[subtask2111, subtask2112])
    subtask212 = Task("subtask212", subtasks=[subtask2121, subtask2122])
    subtask221 = Task("subtask221", subtasks=[subtask2211, subtask2212])
    subtask222 = Task("subtask222", subtasks=[subtask2221, subtask2222])
    # 2
    subtask11 = Task("subtask11", subtasks=[subtask111, subtask112])
    subtask12 = Task("subtask12", subtasks=[subtask121, subtask122])
    subtask21 = Task("subtask21", subtasks=[subtask211, subtask212])
    subtask22 = Task("subtask22", subtasks=[subtask221, subtask222])
    # 1
    subtask1 = Task("subtask1", subtasks=[subtask11, subtask12])
    subtask2 = Task("subtask2", subtasks=[subtask21, subtask22])
    # 0
    task = Task("task", subtasks=[subtask1, subtask2])
    
    task1 = Task(**asdict(task))

    task2 = Task(**asdict(task1))

    print_task(task2)