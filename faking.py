import kivy 
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 

class childApp(GridLayout): 
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = 'Player count '))
        self.player_count = TextInput()
        self.add_widget(self.player_count)

        self.add_widget(Label(text = 'Player name '))
        self.player_name = TextInput()
        self.add_widget(self.player_name)

        self.press = Button(text = "Save name")
        self.press.bind(on_press = self.save_name)
        self.add_widget(self.press)

    def save_name(self, instance): 
        print("Name of player is " + self.player_name.text)
        print("")


class parentApp(App): 
    def build(self):
        return childApp()

if __name__ == "__main__": 
    parentApp().run()