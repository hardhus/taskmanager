from datetime import datetime
from operator import index
import os
import json
from dataclasses import dataclass, asdict, field
from types import ClassMethodDescriptorType
from typing import List, Optional

@dataclass
class Task:
    name: str
    creacted_time: str = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
    subtasks: List["Task"] = None
    def __post_init__(self):
        if self.subtasks is not None:
            self.subtasks = [Task(**subtask) if isinstance(subtask, dict) else subtask for subtask in self.subtasks]
        # 
            # self.subtasks = [Task(subtask.name, subtask.subtasks) for subtask in self.subtasks]

class TaskManager:

    @classmethod
    def Ready(cls, indent=2):
        cls.path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "TaskManager", "tasks.json")
        cls.indent = indent
        cls.checkJsonFile()
        print(cls.path)

    @classmethod
    def getTask(cls, path: str):
        cls.checkJsonFile()
        pass

    @classmethod
    def postTask(cls, data: Task, path: list[int] = []):
        cls.checkJsonFile()
        tasks = json.load(open(cls.path, "r"))
        
        tasks["tasks"] = cls.recursivePostTask(data, path, tasks["tasks"])
        json.dump(tasks, open(cls.path, "w"), indent=cls.indent)

    @classmethod
    def recursivePostTask(cls, data: Task, path: list[int], current_level):
        if len(path) == 0:
            current_level.append(asdict(data))
            return current_level
        if current_level[path[0]]["subtasks"] is None:
            current_level[path[0]]["subtasks"] = []
        current_level[path[0]]["subtasks"] = cls.recursivePostTask(data, path[1:], current_level[path[0]]["subtasks"])
        return current_level
        # lenght = len(path)
        # if lenght == 0:
        #     tasks["tasks"].append(asdict(data))
        # elif lenght == 1:
        #     if tasks["tasks"][path[0]]["subtasks"] is None:
        #         tasks["tasks"][path[0]]["subtasks"] = [] 
        #     tasks["tasks"][path[0]]["subtasks"].append(asdict(data))
        # elif lenght == 2:
        #     if tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"] is None:
        #         tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"] = []
        #     tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"].append(asdict(data))
        # elif lenght == 3:
        #     if tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"] is None:
        #         tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"] = []
        #         tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"].append(asdict(data))
        # print(tasks)
        # json.dump(tasks, open(cls.path, "w"), indent=2)
        # pass

    @classmethod
    def updateTask(cls, path: str, data: Task):
        cls.checkJsonFile()
        pass

    @classmethod
    def deleteTask(cls, path: str):
        cls.checkJsonFile()
        pass

    @classmethod
    def loadTasks(cls, ) -> List[Task]:
        cls.checkJsonFile()
        data = json.load(open(cls.path, "r"))
        tasks = []
        for i in data["tasks"]:
            tasks.append(Task(**i))
        return tasks

    @classmethod
    def checkJsonFile(cls):
        if not os.path.exists(cls.path):
            json.dump({"tasks": []}, open(cls.path, "w"), indent=2)

    @classmethod
    def printTask(cls, task, level=0):
        indentation = "    " * level
        print(f"{indentation}{task.name}:")
        
        if task.subtasks:
            for subtask in task.subtasks:
                if isinstance(subtask, Task):
                    cls.printTask(subtask, level + 1)
                else:
                    print(f"{indentation}    {subtask}")

if __name__ == "__main__":
    TaskManager.Ready(4)

    TaskManager.postTask(Task("ŞEYMA NEREDE?"), [6, 1, 0, 0, 0])

    for i in TaskManager.loadTasks():
        TaskManager.printTask(i)

class TaskManager1:
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
        cls.path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "TaskManager", "tasks.json")
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
        elif taskName in asdict(tasks).keys():
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

    @classmethod
    def getTask(cls):
        pass

def print_task(task, level=0):
        indentation = "    " * level
        print(f"{indentation}{task.name}:")
        
        if task.subtasks:
            for subtask in task.subtasks:
                if isinstance(subtask, Task):
                    print_task(subtask, level + 1)
                else:
                    print(f"{indentation}    {subtask}")

def getTask(path: str):
    checkJsonFile("tasks.json")
    pass

def postTask(data: Task, path: list[int] = []):
    checkJsonFile("tasks.json")
    tasks = json.load(open("tasks.json", "r"))
    lenght = len(path)
    if lenght == 0:
        tasks["tasks"].append(asdict(data))
    elif lenght == 1:
        if tasks["tasks"][path[0]]["subtasks"] is None:
            tasks["tasks"][path[0]]["subtasks"] = [] 
        tasks["tasks"][path[0]]["subtasks"].append(asdict(data))
    elif lenght == 2:
        if tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"] is None:
            tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"] = []
        tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"].append(asdict(data))
    elif lenght == 3:
        if tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"] is None:
            tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"] = []
            tasks["tasks"][path[0]]["subtasks"][path[1]]["subtasks"][path[2]]["subtasks"].append(asdict(data))
    print(tasks)
    json.dump(tasks, open("tasks.json", "w"), indent=2)
    pass

def updateTask(path: str, data: Task):
    checkJsonFile("tasks.json")
    pass

def deleteTask(path: str):
    checkJsonFile("tasks.json")
    pass

def checkJsonFile(path):
    if not os.path.exists(path):
        json.dump({"tasks": []}, open(path, "w"), indent=2)

def loadTasks():
    checkJsonFile("tasks.json")
    data = json.load(open("tasks.json", "r"))
    tasks = Task(data)
    print_task(tasks)

if __name__ == "__main__":
    pass
    # loadTasks()
    # task = Task("Task0", [Task("Task01", [Task("Task011"), Task("Task012")]), Task("Task02", [Task("Task021"), Task("Task022")])])
    # json.dump(asdict(task), open("tasks.json", "w"), indent=2)
    # task = json.load(open("tasks.json", "r"))
    # print(task)
    # task["subtasks"][0]["created_time"] = None
    # json.dump(task, open("tasks.json", "w"), indent=2)
    
    # TaskManager.Ready()
    # TaskManager.addTask(Task("Task0", [Task("Task01", [Task("Task011"), Task("Task012")]), Task("Task02", [Task("Task021"), Task("Task022")])]))
    # TaskManager.addTask("ŞEYMA NEREDE?")
    # print(TaskManager.loadTasks()[1])
    # # 4
    # subtask1111 = Task("subtask1111")
    # subtask1112 = Task("subtask1112")
    # subtask1121 = Task("subtask1121")
    # subtask1122 = Task("subtask1122")
    # subtask1211 = Task("subtask1211")
    # subtask1212 = Task("subtask1212")
    # subtask1221 = Task("subtask1221")
    # subtask1222 = Task("subtask1222")
    # subtask2111 = Task("subtask2111")
    # subtask2112 = Task("subtask2112")
    # subtask2121 = Task("subtask2121")
    # subtask2122 = Task("subtask2122")
    # subtask2211 = Task("subtask2211")
    # subtask2212 = Task("subtask2212")
    # subtask2221 = Task("subtask2221")
    # subtask2222 = Task("subtask2222")

    # # 3
    # subtask111 = Task("subtask111", subtasks=[subtask1111, subtask1112])
    # subtask112 = Task("subtask112", subtasks=[subtask1121, subtask1122])
    # subtask121 = Task("subtask121", subtasks=[subtask1211, subtask1212])
    # subtask122 = Task("subtask122", subtasks=[subtask1221, subtask1222])
    # subtask211 = Task("subtask211", subtasks=[subtask2111, subtask2112])
    # subtask212 = Task("subtask212", subtasks=[subtask2121, subtask2122])
    # subtask221 = Task("subtask221", subtasks=[subtask2211, subtask2212])
    # subtask222 = Task("subtask222", subtasks=[subtask2221, subtask2222])
    # # 2
    # subtask11 = Task("subtask11", subtasks=[subtask111, subtask112])
    # subtask12 = Task("subtask12", subtasks=[subtask121, subtask122])
    # subtask21 = Task("subtask21", subtasks=[subtask211, subtask212])
    # subtask22 = Task("subtask22", subtasks=[subtask221, subtask222])
    # # 1
    # subtask1 = Task("subtask1", subtasks=[subtask11, subtask12])
    # subtask2 = Task("subtask2", subtasks=[subtask21, subtask22])
    # # 0
    # task = Task("Şeyma", subtasks=[subtask1, subtask2])
    
    # task1 = Task(**asdict(task))

    # task2 = Task(**asdict(task1))

    # print_task(task2)