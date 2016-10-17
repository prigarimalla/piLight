from datetime import datetime, timedelta
from LightSetter import LightSetter
from apscheduler.schedulers.background import BackgroundScheduler

class LightScheduler(object):
    def __init__(self):
        self.setter = LightSetter()
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def setLights(self, color):
        self.setter.setLights(color)

    def setScheduledLights(self, color):
        print 'running'
        self.setLights(color)

    def setEvent(self, secondsUntilEvent, color):
        eventTime = datetime.now()+timedelta(seconds=secondsUntilEvent)
        eventId = str(hash((eventTime, color)))
        self.scheduler.add_job(self.setScheduledLights, args=(color,), next_run_time=eventTime, id=eventId)
        return eventId

    def cancelEvent(self, eventId):
        self.scheduler.remove_job(eventId)
