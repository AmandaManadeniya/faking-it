from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
import helpers
from kivy.lang import Builder
from nltk.corpus import wordnet as wn
import random


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()

        self.username = Builder.load_string(helpers.username_input)
        btn_flat = MDRectangleFlatButton(text='Submit',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_release=self.show_data)

        name_btn = MDRectangleFlatButton(text='Generate random name',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                         on_release=self.random_name)

        screen.add_widget(btn_flat)
        screen.add_widget(name_btn)
        screen.add_widget(self.username)
        return screen

    def show_data(self,obj):
        print(self.username.text)

    def random_name(self,obj): 

        rand_name = ["Popular Pete", "Mellow Mel", "Jiggly James", "Naughty Niko", "Astute AJ", "Sloppy Sharky", "Silly Sally" ]

        print(random.choice(rand_name))

DemoApp().run()