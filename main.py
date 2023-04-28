import distutils.dir_util
import glob
import json
import logging
import os
import pathlib
import sys
import time
import runpy
import shutil
import tempfile
import string
import secrets
import textwrap
import functools
import subprocess
from dirsync import sync
from pathlib import Path
#from plyer import storagepath

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.textfield import MDTextField

from kivymd.uix.menu import MDDropdownMenu
#from plyer import storagepath
#from android.permissions import request_permissions, Permission

# Setup Kivy logging
log_to_txt = 0
# Setup Kivy Logging
log_dir = os.getcwd()
log_file = os.path.join(log_dir, "logs", "kivy.txt")
log_file = "logs/kivy.txt"

if log_to_txt:
    if os.path.exists(log_file):
        try:
            os.remove(log_file)
            time.sleep(.5)
            Path(log_file).touch()
        except Exception as e:
            pass
    Logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")
    )
    Logger.addHandler(file_handler)



# Load KV Data
with open("main.yaml", "r") as file:
    KV = file.read()


class LogHandler(logging.Handler):
    def __init__(self, debug_console):
        super().__init__()
        self.debug_console = debug_console

    def emit(self, record):
        msg = self.format(record)
        self.debug_console.text += f"{msg}\n"


class MainScreen(Screen):
    pass


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.screen_manager = Builder.load_string(KV)
        self.menu_items = [
            {
                "text": "Main Screen",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="main_screen": self.change_screen(x),
            },
            {
                "text": "Add App",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="screen_one": self.change_screen(x),
            },
            {
                "text": "View Logs",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="screen_two": self.change_screen(x),
            },
            {
                "text": "Exit",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="exit": self.kill_app(x),
            },
        ]
        self.dropdown_menu = MDDropdownMenu(
            caller=self.screen_manager.get_screen("main_screen").ids.top_bar,
            items=self.menu_items,
            width_mult=3,
        )
        return self.screen_manager

    def on_start(self):
        main_screen = self.screen_manager.get_screen("main_screen")
        debug_console = main_screen.ids["debug_console"]
        handler = LogHandler(debug_console)
        logging.getLogger().addHandler(handler)
        # Setup File Manager
        #start_path = storagepath.get_external_storage_dir()
        start_path = "/storage/emulated/150"
        screen_one = self.screen_manager.get_screen("screen_one")
        screen_one.ids.app_src.text = start_path
        self.log_app("Starting Launcher")

        f = "apps.json"
        file_exists = os.path.exists(f)
        if file_exists:
            pass
        else:
            jd = {}
            jd["data"] = {}
            jd["data"]["apps"] = []
            with open(f, "w") as outfile:
                json.dump(jd, outfile)
        self.load_apps()

    def log_app(self, msg):  # Set default log level to 20 (INFO)
        Logger.log(20, f"{msg}")
        self.screen_manager.get_screen("main_screen").ids["debug_console"].text += "\n"

    def kill_app(self, x):
        sys.exit()

    def switch_screen(self, screen_name):
        self.root.current = screen_name

    def right_dots(self):
        self.dropdown_menu.caller = self.screen_manager.current_screen.ids.top_bar
        self.dropdown_menu.open()

    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name
        self.dropdown_menu.dismiss()

    def update_labels(self, text):
        main_screen = self.screen_manager.get_screen("main_screen")
        main_screen.ids.main_label_1.text = text
        main_screen.ids.main_label_2.text = text
        self.change_screen("main_screen")

    # File Manager
    def file_manager_open(self):
        #start_path = os.getcwd()
        #start_path = app_storage_path("external")
        #start_path = storagepath.get_external_storage_dir()
        start_path = "/storage/emulated/150"
        self.file_manager.show(os.path.expanduser(f"{start_path}"))
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        screen_one = self.screen_manager.get_screen("screen_one")
        screen_one.ids.app_src.text = path
        folder = os.path.dirname(path)
        screen_one.ids.app_name.text = os.path.basename(folder)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    # Add Applications
    def app_clear(self):
        screen_one = self.screen_manager.get_screen("screen_one")
        screen_one.ids.app_name.text = ""
        screen_one.ids.app_src.text = ""
        screen_one.ids.info_card.opacity = 0
        screen_one.ids.info_message.text = ""

    def on_submit(self):
        screen_one = self.screen_manager.get_screen("screen_one")
        screen_one.ids.info_card.opacity = 1
        data = {}
        app_name = screen_one.ids.app_name.text
        data["app_name"] = app_name.strip()
        app_src = screen_one.ids.app_src.text
        data["app_src"] = os.path.dirname(app_src)
        cwd = os.getcwd()
        characters = string.ascii_letters + string.digits
        rando = "".join(secrets.choice(characters) for _ in range(6))
        rando = f"a{rando}"
        rando = rando.lower()
        app_dst = os.path.join(cwd, "apps", rando)
        data["app_dst"] = app_dst
        data["app_id"] = rando

        fail = 0
        notice = ""
        if len(data["app_name"]) < 3:
            fail = 1
            notice += chr(8226) + " App name must be at least 3 characters \n\n"
        if not os.path.isdir(data["app_src"]):
            fail = 1
            notice += chr(8226) + " Invalid App Source directory \n\n"

        if fail == 0:
            txt = "App Added: \n\n"
            for k, v in data.items():
                txt += f"{k}: {v} \n"
            self.update_apps(data)
        else:
            txt = notice

        screen_one.ids.info_message.text = txt

    def update_apps(self, new_dict):
        with open("apps.json", "r") as f:
            data = json.load(f)
        apps = data["data"]["apps"]
        for app in apps:
            if app["app_src"] == new_dict["app_src"]:
                app.update(new_dict)
                break
        else:  # no break, so no existing app found, add the new one to the list of apps
            apps.append(new_dict)
        with open("apps.json", "w") as f:
            json.dump(data, f)

    def load_apps(self):
        self.log_app("Loading Apps")
        main_screen = self.screen_manager.get_screen("main_screen")
        app_list = main_screen.ids["app_list"]
        app_list.clear_widgets()

        apps_found = False
        with open("apps.json", "r") as f:
            data = json.load(f)
        apps = data["data"]["apps"]
        card_id = 1
        for app in apps:
            apps_found = True
            d = dict(app)
            app_name = d["app_name"]
            app_dst = d["app_dst"]
            app_id = d["app_id"]
            exe = os.path.join(app_dst, "main.py")
            the_card = self.new_card(app_name, card_id, app_id)
            app_list.add_widget(the_card)
            card_id += 1
            self.log_app(f"Loaded app {app_name}")

        if not apps_found:
            logging.warning("No apps found")

    def new_card(self, app_name, card_id, app_id):
        card_id_str = str(card_id)
        the_card_id = f"card_{card_id_str}"
        card_template = textwrap.dedent(
            """
            MDCard:
                id: app_card_|card_id|
                orientation: 'vertical'
                size_hint: 0.99, None
                height: content.height + dp(40)
                padding: [dp(4),0,dp(4),dp(4)]
                #spacing: dp(10)
                elevation: 0
                radius: [25, 25, 25, 25]
                canvas.before:
                    Color:
                        rgba: app.theme_cls.primary_color
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [25, 25, 25, 25]
                    Color:
                        rgba: app.theme_cls.primary_color
                    Line:
                        rounded_rectangle: self.x, self.y, self.width, self.height, 25, 25, 25, 25
                        width: 2
            
                MDBoxLayout:
                    id: content
                    orientation: "vertical"
                    size_hint_y: None
                    adaptive_height: True
                    padding: [dp(4), dp(-14), dp(4), dp(4)] 
            
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: app_name.height
                        padding: dp(5)
                        spacing: dp(5)
            
                        BoxLayout:
                            size_hint_x: 0.5
                            padding: 0
                            spacing: 0
            
                            MDLabel:
                                id: app_name
                                text: "|app_name|"
                                font_style: "H6"
                                halign: "left"
                                
                        BoxLayout:
                            size_hint_x: 0.5
                            padding: 0
                            spacing: 0
            
                            MDLabel:
                                id: app_date
                                text: "2023-04-23"
                                font_style: "H6"
                                halign: "right"
                            
            
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(50)
                        pos_hint: {"bottom": 1}
            
                        BoxLayout:
                            size_hint_x: 0.7
            
                        MDRoundFlatButton:
                            text: "Delete"
                            #on_release: app.del_app(app_id)
                            on_release: app.del_app("|app_id|")
                        
                        Widget:
                        
                        MDRoundFlatButton:
                            text: "Sync"
                            on_release: app.sync_app("|app_id|")
            
                        MDRoundFlatButton:
                            text: "Run"
                            on_release: app.run_app("|app_id|")
                            
                        MDRoundFlatButton:
                            text: "Sync & Run"
                            on_release: app.syncrun_app("|app_id|")
        """
        )
        card_template = card_template.replace("|app_name|", app_name)
        card_template = card_template.replace("|card_id|", card_id_str)
        card_template = card_template.replace("|app_id|", app_id)

        try:
            the_card = Builder.load_string(card_template)
        except Exception as e:
            err = str(e)
            logger.error(f"Error loading KV string: {str(e)}")
            logger.error(traceback.format_exc())
        return the_card
    
    def get_app_by_id(self, app_id):
        with open('apps.json', 'r') as file:
            data = json.load(file)
        for app in data['data']['apps']:
            if app['app_id'] == app_id:
                return dict(app)
        return None
   
    def del_app(self, app_id):
        self.log_app(f"Deleting {app_id}")
        # Load the JSON file
        with open('apps.json', 'r') as f:
            data = json.load(f)
    
        app_to_delete = None
    
        # Find the app by app_id
        for app in data['data']['apps']:
            if app['app_id'] == app_id:
                app_to_delete = app
                break
    
        if app_to_delete:
            # Remove the app from the list
            data['data']['apps'].remove(app_to_delete)
    
            # Write the updated JSON back to the file
            with open('apps.json', 'w') as f:
                json.dump(data, f)
    
            # Delete the app_dst directory
            app_dst = app_to_delete['app_dst']
            if os.path.exists(app_dst):
                shutil.rmtree(app_dst)
            show = f"App with ID '{app_id}' has been deleted."
            self.log_app(f"{show}")
        else:
            show = f"No app found with ID '{app_id}'."
            self.log_app(f"{show}")
        self.load_apps()
        
    def sync_app(self, app_id):
        self.log_app(f"Syncing {app_id}")
        app_data = self.get_app_by_id(app_id)
        src = app_data["app_src"]
        dst = app_data["app_dst"]
        # Set up synchronization options
        action = 'sync'  # Options are 'sync', 'diff', or 'update'
        # 'sync': Synchronize the directories
        # 'diff': Show the differences between the directories
        # 'update': Update the target directory with the latest changes from the source directory
        bidirectional = False  # Set to True for bidirectional sync
        verbose = True  # Set to True for detailed output
        purge = True  # Set to True to remove files in target not present in source
        # Perform the directory synchronization
        if not os.path.exists(dst):
            os.makedirs(dst)
        sync(src, dst, action=action, twoway=bidirectional, verbose=verbose, purge=purge)
        
    def run_kivy_app(self, exe):
        try:
            #runpy.run_path(path_name=exe, run_name="__main__")
            subprocess.Popen(["python3", exe])
        except Exception as e:
            err = str(e)
            show = f"Error running Kivy app '{exe}': {err}"
            self.log_app(f"{show}")
        
    def run_app(self, app_id):
        self.log_app(f"Running {app_id}")
        app_data = self.get_app_by_id(app_id)
        dst = app_data["app_dst"]
        exe = os.path.join(dst, "main.py")
        self.log_app(f"Running {exe}")
        self.run_kivy_app(exe)
    
    def syncrun_app(self, app_id):
        self.log_app(f"Syncing & Running {app_id}")

if __name__ == "__main__":
    MyApp().run()
    
