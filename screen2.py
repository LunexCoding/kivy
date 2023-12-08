from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.add_widget(Button(text='Switch to Screen 1', on_press=self.switch_screen))

    def switch_screen(self, instance):
        self.manager.current = 'screen1'
