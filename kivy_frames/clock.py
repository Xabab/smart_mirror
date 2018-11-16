from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock as Cl
import datetime

class Clock(BoxLayout):
    def __init__(self, *args, **kwargs):
        BoxLayout.__init__(self, *args, **kwargs)
        self.formattedTime = ''
        #self.formattedDate = ''

        Cl.schedule_once(self.update, 0)


    def update(self, *args):
        #                                      например, "22:30"
        formattedTime = datetime.datetime.now().strftime("%H:%M")
        ##                                      например, "08 November, 2018"
        #formattedDate = datetime.datetime.now().strftime("%d %B, %Y")

        # обновляем содержимое лейблов даты и времени
        if formattedTime != self.formattedTime:
            self.formattedTime = formattedTime
            self.ids["clock"].text = formattedTime

        #if formattedDate != self.formattedDate:
        #    self.formattedDate = formattedDate
        #    self.dateLabel.config(text=formattedDate)

        # выполняем апдейт 10 раз/секунду
        #self.timeLabel.after(100, self.update)

    def _update_system_time(self):
        pass
