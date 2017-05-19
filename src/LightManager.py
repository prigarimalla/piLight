from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from src.config.lightConfig import zones

class LightManager(object):
    def __init__(self):
        self.setterZones = zones
        self.defaultSetterZone = self.setterZones[0]
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def setLights(self, color, zone=None):
        if not zone:
            self.defaultSetterZone.setLights(color)
        elif int(zone) in range(len(self.setterZones)):
            self.setterZones[int(zone)].setLights(color)
        else:
            raise InvalidZoneException

    def setEvent(self, secondsUntilEvent, color, zone=None):
        eventTime = datetime.now()+timedelta(seconds=secondsUntilEvent)
        eventId = str(hash((eventTime, color)))
        self.scheduler.add_job(self.setLights, args=(color,zone), next_run_time=eventTime, id=eventId)
        return eventId

    def cancelEvent(self, eventId):
        self.scheduler.remove_job(eventId)

    def getZoneInfo(self):
        return {str(i): {'type': zone.mode, 'description': zone.description} for i, zone in zip(range(len(self.setterZones)), self.setterZones)}

class InvalidZoneException(Exception):
    def __str__(self):
        return 'Event specified invalid zone'