from datetime import datetime, date, time
from astral import Astral
from bisect import bisect

class sunEventGenerator(object):
	def __init__(self, city='Dallas', color=(255,153,0)):
		self.city = Astral()[city]
		self.color = color
		#Times at which to toggle the lights. By convention, lights are
		#off at midnight, and the first event is a toggle on. 
		self.eventList = [time(5,30), time(13,00), self.city.sunset().time(), time(22,30)]
		#Intentionally setting isOn to the opposite value to ensure that
		#on the first poll the color is set appropriately. 
		self.isOn = bisect(self.eventList,datetime.today().time())%2 == 0

	def getEvent(self):
		if self.isOn == (bisect(self.eventList,datetime.today().time())%2 != 0):
			return (-1,-1,-1) #(-1,-1,-1) is the Do Nothing color. 
		self.isOn = not self.isOn
		return self.color if self.isOn else (0,0,0)

