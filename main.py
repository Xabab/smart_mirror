from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

import cProfile, pstats, io

from kivy_frames.utils import BasicWidget
from kivy_frames.weather import Weather
from kivy_frames.calendar import Calendar
from kivy_frames.clock import Clock
from kivy_frames.events import Events
from kivy_frames.exchangeRates import ExchangeRates
from kivy_frames.mail import Mail
from kivy_frames.news import News


class Root(GridLayout):
    display = ObjectProperty()


class MainApp(App):
    def build(self):
        self.title = 'SmartMirror'
        return Root()

    def on_start(self):
        self.profile = cProfile.Profile()
        self.profile.enable()

    def on_stop(self):
        self.profile.disable()
        s = io.StringIO()
        #sortby = cumtime
        ps = pstats.Stats(self.profile, stream=s).sort_stats("time")
        ps = ps.reverse_order()
        ps.print_stats()
        print(s.getvalue())
        self.profile.dump_stats('sm.profile')

        print("\n\nMEANT TO BE EXECUTED IN PORTRAIT MODE (desktop pc)\n\n")



if __name__ == "__main__":
    '''
    import subprocess
    import re
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    resolution = [int(s) for s in re.findall(r"\d+", output)]           #[800, 600]
    '''

    from kivy.core.window import Window
    # Window.fullscreen = True
    Window.fullscreen = 'auto'


    from os import listdir
    kv_path = './kv/'
    for kv in listdir(kv_path):
        if(kv == "__pycache__"):
            continue
        Builder.load_file(kv_path + kv)

    app = MainApp()
    app.run()
