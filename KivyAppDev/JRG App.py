from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
import kivy

class ScreenManagement(ScreenManager):
    pass

class Login(Screen):
    pass

class Logincheck(Widget):
    def check(self, user, pw):
        if user == 'James' and pw == 'mak':
            app.root.current='login'
        

class Game(Screen):
    pass

class Control(Widget):
    def on_touch_down(self, touch):
        pass



presentation = Builder.load_file('JRG.kv')


class JRGApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    JRGApp().run()
