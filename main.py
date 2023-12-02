from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screen1 import Screen1  # Import the first screen module
from screen2 import Screen2  # Import the second screen module


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))

        return sm


if __name__ == '__main__':
    MyApp().run()
