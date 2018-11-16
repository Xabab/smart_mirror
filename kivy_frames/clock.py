import math

from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock as Cl
import datetime

class Clock(BoxLayout):
    iteration = 0

    def __init__(self, *args, **kwargs):
        BoxLayout.__init__(self, *args, **kwargs)
        self.formattedTime = ''

        Cl.schedule_interval(self.update, 0.25)


    def update(self, *args):

        if math.floor(self.iteration/2) == 0:
            #                                      например, "22:30"
            formattedTime = datetime.datetime.now().strftime("%H:%M")
        else:
            #                                      например, "22 30"
            formattedTime = datetime.datetime.now().strftime("%H %M")

        self.iteration += 1

        if self.iteration > 3:
            self.iteration = 0

        if formattedTime != self.formattedTime:
            self.formattedTime = formattedTime
            self.ids["clock0"].text = formattedTime

