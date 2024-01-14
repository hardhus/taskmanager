import os
import customtkinter as ctk
from PIL import Image
from .SideBarFrame import SideBarFrame
from .TodayFrame import TodayFrame
from .Important import ImportantFrame
from .Scheduled import ScheduledFrame

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.wm_title("Task Manager")
        self.geometry("900x600-8-1")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        imgPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "assets")

        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(imgPath, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(
            light_image=Image.open(os.path.join(imgPath, "home_dark.png")),
            dark_image=Image.open(os.path.join(imgPath, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(
            light_image=Image.open(os.path.join(imgPath, "chat_dark.png")),
            dark_image=Image.open(os.path.join(imgPath, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(
            light_image=Image.open(os.path.join(imgPath, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(imgPath, "add_user_light.png")), size=(20, 20))

        self.todayFrame = TodayFrame(self, corner_radius=0, fg_color="transparent")
        self.importantFrame = ImportantFrame(self, corner_radius=0, fg_color="transparent")
        self.scheduledFrame = ScheduledFrame(self, corner_radius=0, fg_color="transparent")

        self.sideBarFrame = SideBarFrame(self, corner_radius=0)
        self.sideBarFrame.grid(row=0, column=0, sticky="nsew")