import datetime

from kivy.uix.boxlayout import BoxLayout

from kivy_frames.basicWidget import BasicWidget
from kivy.clock import Clock


class Calendar(BoxLayout):
    def __init__(self, *args, **kwargs):
        BoxLayout.__init__(self, *args, **kwargs)
        self.formattedDate = ''

        Clock.schedule_interval(self.update, 0.25)


    def update(self, *args):
        # #                                      например, "08 November, 2018"
        #                                      например, "08 Nov"
        formattedDate = datetime.datetime.now().strftime("%d %B, %Y")[0:6]

        # обновляем содержимое лейблов даты и времени
        if formattedDate != self.formattedDate:
            self.formattedDate = formattedDate
            self.ids["date"].text = formattedDate
