import customtkinter as ctk
from typing import Tuple, Any

class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.master = master

        self.btnTodayFrame = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Today",
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        image=master.home_image, anchor="w", command=self.TodayFrameEvent)
        self.btnTodayFrame.grid(row=1, column=0, sticky="nsew")

        self.btnImportantFrame = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Important",
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        image=master.chat_image, anchor="w", command=self.ImportantFrameEvent)
        self.btnImportantFrame.grid(row=2, column=0, sticky="nsew")

        self.btnScheduledFrame = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Scheduled",
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        image=master.add_user_image, anchor="w", command=self.ScheduledFrameEvent)
        self.btnScheduledFrame.grid(row=3, column=0, sticky="nsew")

        self.switchModeVar = ctk.StringVar(value="on")
        self.switchMode = ctk.CTkSwitch(self, command=self.switchModeEvent, onvalue="on", offvalue="off", text="Dark Mode", variable=self.switchModeVar, progress_color="transparent")
        self.switchMode.grid(row=4, column=0, sticky="nsew", padx=10, pady=430)

        self.selectFrameByName("TodayFrame")

    def switchModeEvent(self):
        if self.switchMode.get() == "on":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def TodayFrameEvent(self):
        self.selectFrameByName("TodayFrame")

    def ImportantFrameEvent(self):
        self.selectFrameByName("ImportantFrame")

    def ScheduledFrameEvent(self):
        self.selectFrameByName("ScheduledFrame")

    def selectFrameByName(self, frameName):
        self.btnTodayFrame.configure(fg_color=("gray75", "gray25") if frameName == "TodayFrame" else "transparent")
        self.btnImportantFrame.configure(fg_color=("gray75", "gray25") if frameName == "ImportantFrame" else "transparent")
        self.btnScheduledFrame.configure(fg_color=("gray75", "gray25") if frameName == "ScheduledFrame" else "transparent")

        if frameName == "TodayFrame":
            self.master.todayFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.master.todayFrame.grid_forget()
        if frameName == "ImportantFrame":
            self.master.importantFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.master.importantFrame.grid_forget()
        if frameName == "ScheduledFrame":
            self.master.scheduledFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.master.scheduledFrame.grid_forget()