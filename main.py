from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Interface(FloatLayout):
    
    def displayInfo(self):
        data = self.ids.textInput.text
        self.ids.label.text = data

class ProjectApp(App):
    pass

ProjectApp().run()