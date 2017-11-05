from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
##from kivy.uix.gridlaybout import GridLayout
##from kivy.uix.textinput import TextImput
##import kivy
##
##class LoginScreen(GridLayout):
##    def __init__(self, **kwargs):
##        super(LoginScreen, self).__init__(**kwargs)
##        self.cols = 2
##        
##        self.add_widget(Label(text="Username:"))
##        self.username = TextInput(multiline=False)
##        self.add_widget(self.username)
##
##        self.add_widget(Label(text="Password:"))
##        self.password = TextInput(multiline=False, password=True)
##        self.add_widget(self.password)

class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud['line']=Line(points=(touch.x,touch.y))
            
        
    def on_touch_move(self, touch):
        print(touch)
        touch.ud['line'].points += (touch.x,touch.y)
        
    def on_touch_up(self, touch):
        print(touch)


class ScreenManagement(ScreenManager):
    pass
 
class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    def f(self):
        return FloatLayout()




presentation = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()
