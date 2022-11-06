from tkinter import VERTICAL
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

class BoxLayoutExample(BoxLayout): 
    pass 
"""
    def __init__(self, **kwargs): #**kwargs --> needed for kivy --> we can ignore 
        super().__init__(**kwargs) 
        self.orientation = "vertical"
        b1 = Button(text = "Save name")
        self.add_widget(b1)
"""

class MainWidget(Widget): 
    pass 

class LabApp(App): 
    pass

LabApp().run()