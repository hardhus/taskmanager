import customtkinter as ctk
from typing import Tuple, Any
from .TaskManager import TaskManager

class TodayFrame(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.master = master
        self._fg_color = fg_color

        self.frame = ctk.CTkScrollableFrame(self, label_text="Today Frame", width=500, height=300)
        self.frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        self.loadTasks()

        self.entryAddTask = ctk.CTkEntry(self, placeholder_text="Add Task")
        self.entryAddTask.bind("<Return>", self.AddTaskEvent)
        self.entryAddTask.pack(side=ctk.BOTTOM, fill=ctk.X,padx=10, pady=10)

    def AddTaskEvent(self, event):
        taskName = "Task" if self.entryAddTask.get() == "" else self.entryAddTask.get()
        ctk.CTkButton(self.frame, text=taskName, fg_color=("gray75", "gray25"), corner_radius=10).pack(padx=5, pady=5)
        self.entryAddTask.delete(0, ctk.END)

    def loadTasks(self):
        err, tasks = TaskManager.loadTasks()
        if err is not None:
            print(err)
        for i, taskName in enumerate(tasks.keys()):
            ctk.CTkCheckBox(self.frame, text="").grid(row=i,column=0, padx=5, pady=5, sticky=ctk.NSEW)
            ctk.CTkButton(self.frame, text=taskName, fg_color=("gray75", "gray25"), corner_radius=10).grid(
                row=i, column=1, padx=5, pady=5, sticky=ctk.NSEW)