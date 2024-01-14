import customtkinter as ctk
from typing import Tuple, Any

class TodayFrame(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.master = master
        self._fg_color = fg_color

        self.label = ctk.CTkLabel(self, text="Today Frame", fg_color=("gray75", "gray25"), corner_radius=10)
        self.label.pack()

        self.entryAddTask = ctk.CTkEntry(self, placeholder_text="Add Task")
        self.entryAddTask.bind("<Return>", self.AddTaskEvent)
        self.entryAddTask.pack(side=ctk.BOTTOM, fill="both", padx=10, pady=10)

    def AddTaskEvent(self, event):
        taskName = "Task" if self.entryAddTask.get() == "" else self.entryAddTask.get()
        ctk.CTkButton(self, text=taskName, fg_color=("gray75", "gray25"), corner_radius=10).pack(padx=5, pady=5)
        self.entryAddTask.delete(0, ctk.END)