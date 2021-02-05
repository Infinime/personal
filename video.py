from kivy.app import App
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer

kv = Builder.load_file('video.kv')


class VidPlay(VideoPlayer):
    # pattern=re.compile(r'C:\Users\hp\Videos\Series\Titans\Titans S01E')
    vidnames = {'01', '02', '03', '04', '05',
                '06', '07', '08', '09', '10', '11'}
    """docstring for VidPlay"""
    filename = r'C:\Users\gtcan\Documents\Python\Gesaffelstein _ The Weeknd - Lost in the Fire (Off(1080P_HD).mp4'
    print(filename)


class VideoPlayerApp(App):
    def build(self):
        return VidPlay()


if __name__ == '__main__':
    VideoPlayerApp().run()
