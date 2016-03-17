from datetime import datetime, date, time, timedelta
from astral import Astral
from bisect import bisect

class sunEventGenerator(object):
    def __init__(self, city='Dallas', color=(255,255,255)):
        self.city = Astral()[city]
        self.color = color
        #Time when sunset was last updated
        self.lastUpdate = datetime.today()
        #Times at which to toggle the lights. By convention, lights are
        #off at midnight, and the first event is a toggle on.
        self.eventList = self.updateEventList()
        #Frequency of how often to update evenList (Here it is every day)
        self.updateFreq = timedelta(1)
        #Intentionally setting isOn to the opposite value to ensure that
        #on the first poll the color is set appropriately.
        self.isOn = bisect(self.eventList,datetime.today().time())%2 == 0

    def getEvent(self):
        if datetime.today() - self.lastUpdate > self.updateFreq:
            self.updateEventList()
        if self.isOn == (bisect(self.eventList,datetime.today().time())%2 != 0):
            return (-1,-1,-1) #(-1,-1,-1) is the Do Nothing color.
        self.isOn = not self.isOn
        return self.color if self.isOn else (0,0,0)

    def updateEventList(self):
        self.eventList = [time(5,30), time(13,00), self.city.sunset().time(), time(22,30)]
        self.lastUpdate = datetime.today()

