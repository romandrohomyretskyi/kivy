from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class FirstScreen(Screen):
    def __init__(self,name ='first'):
        super().__init__(name = name)
        btn = Button(text = 'First Button!')
        btn.on_press = self.next
    def next (self):
        self.manager.transtion.direction = 'up'
        self.manager.current = 'second'
class SecondScreen(Screen):
    def __init__(self, name = 'secomd'):
        super().__init__(name = name)
        btn = Button(text = 'Second button!')
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next (self):
        self.manager.transtion.direction = 'left'
        self.manager.current = 'first'

class MyApp (App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        return sm


MyApp().run()