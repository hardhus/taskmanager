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
    def getTask(cls, path: str):
        cls.checkJsonFile()

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

    @classmethod
    def updateTask(cls, path: str, data: Task):
        cls.checkJsonFile()

    @classmethod
    def deleteTask(cls, path: str):
        cls.checkJsonFile()

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