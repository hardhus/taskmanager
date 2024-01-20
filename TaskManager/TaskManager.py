from datetime import datetime
import os
import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Task:
    name: str
    creacted_time: str = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
    subtasks: List["Task"] = None
    def __post_init__(self):
        if self.subtasks is not None:
            self.subtasks = [Task(**subtask) if isinstance(subtask, dict) else subtask for subtask in self.subtasks]

class TaskManager:
    @classmethod
    def Ready(cls, indent=2):
        cls.path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "TaskManager", "tasks.json")
        cls.indent = indent
        cls.checkJsonFile()

    @classmethod
    def getTask(cls, path: list[int]):
        cls.checkJsonFile()
        tasks = [asdict(i) for i in cls.loadTasks()]

        task = cls.recursiveGetTask(path, tasks)
        return task

    @classmethod
    def recursiveGetTask(cls, path: list[int], tasks: list):
        if len(path) == 1:
            cls.printTask(Task(**tasks[path[0]]))
            return tasks[path[0]]
        cls.recursiveGetTask(path[1:], tasks[path[0]]["subtasks"])

    @classmethod
    def postTask(cls, data: Task, path: list[int] = []):
        cls.checkJsonFile()
        with open(cls.path, "r") as file:
            tasks = json.load(file)
        
        tasks["tasks"] = cls.recursivePostTask(data, path, tasks["tasks"])
        with open(cls.path, "w") as file:
            json.dump(tasks, file, indent=cls.indent)

    @classmethod
    def recursivePostTask(cls, data: Task, path: list[int], current_level):
        if len(path) == 0:
            current_level.append(asdict(data))
            return current_level
        if current_level[path[0]]["subtasks"] is None:
            current_level[path[0]]["subtasks"] = []
        current_level[path[0]]["subtasks"] = cls.recursivePostTask(data, path[1:], current_level[path[0]]["subtasks"])
        return current_level

    @classmethod
    def updateTask(cls, data: Task, path: List[int]):
        cls.checkJsonFile()
        with open(cls.path, "r") as file:
            tasks = json.load(file)
        
        tasks["tasks"] = cls.recursiveUpdateTask(data, path, tasks["tasks"])
        with open(cls.path, "w") as file:
            json.dump(tasks, file, indent=cls.indent)

    @classmethod
    def recursiveUpdateTask(cls, data: Task, path: list[int], current_level):
        if len(path) == 1:
            if current_level[path[0]]["subtasks"] is not None:
                data.subtasks = current_level[path[0]]["subtasks"] 
                current_level[path[0]] = asdict(data)
            return current_level
        current_level[path[0]]["subtasks"] = cls.recursiveUpdateTask(data, path[1:], current_level[path[0]]["subtasks"])
        return current_level

    @classmethod
    def deleteTask(cls, path: str):
        cls.checkJsonFile()
        with open(cls.path, "r") as file:
            tasks = json.load(file)

        tasks["tasks"] = cls.recursiveDeleteTask(path, tasks["tasks"])
        with open(cls.path, "w") as file:
            json.dump(tasks, file, indent=cls.indent)

    @classmethod
    def recursiveDeleteTask(cls, path: list[int], current_level):
        if len(path) == 1:
            del current_level[path[0]]
            if len(current_level) == 0:
                return None
            else:
                return current_level
        current_level[path[0]]["subtasks"] = cls.recursiveDeleteTask(path[1:], current_level[path[0]]["subtasks"])
        return current_level

    @classmethod
    def loadTasks(cls) -> List[Task]:
        cls.checkJsonFile()
        with open(cls.path, "r") as file:
            data = json.load(file)
        tasks = []
        for i in data["tasks"]:
            tasks.append(Task(**i))
        return tasks

    @classmethod
    def checkJsonFile(cls):
        if not os.path.exists(cls.path):
            with open(cls.path, "w") as file:
                json.dump({"tasks": []}, file, indent=2)
        try:
            with open(cls.path, "r") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            tasks = {"tasks": []}
            with open(cls.path, "w") as file:
                json.dump(tasks, file, indent=2)
        

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

    TaskManager.deleteTask([0, 0])

    print("*********************************************************************")
    for i in TaskManager.loadTasks():
        TaskManager.printTask(i)