import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.atlas import Atlas
from kivy.uix.button import Button
from kivy.garden.mapview import MapView
from kivy.core.window import Window
Window.clearcolor = (.81, .81, .81, 0.5)

kv=Builder.load_file('action.kv')

atlas=Atlas('C:/Users/hp/AppData/Local/Programs/Python/Python37/Lib/site-packages/kivy/data/images/defaulttheme.atlas')

print(atlas.textures.keys())

class VideoPlayerApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    VideoPlayerApp().run()