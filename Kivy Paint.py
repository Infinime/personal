from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class main(BoxLayout):
    pass

class MainApp(MDApp):
    kv_file="paint.kv"
    def build(self):
        return main()

MainApp().run()