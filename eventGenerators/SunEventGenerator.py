from datetime import datetime, timedelta
from astral import Astral
import requests, time, sys

class SunEventGenerator(object):
    def __init__(self, city, baseUrl, value, zone=0):
        self.city = Astral()[city]
        self.url = baseUrl+'/setEvent/'
        self.value = value
        self.zone = zone

    def setSunset(self):
        return self._setEvent('sunset')

    def setSunrise(self):
        return self._setEvent('sunrise')

    def _setEvent(self, event):
        params = {}
        if isinstance(self.value, int):
            params['mono'] = self.value
        else:
            params['red'] = self.value[0]
            params['green'] = self.value[1]
            params['blue'] = self.value[2]
        params['delay'] = self._secondsUntilSunEvent(event)
        params['zone'] = self.zone
        return requests.get(url=self.url, params=params)

    def secondsUntilSunset(self):
        return self._secondsUntilSunEvent('sunset')

    def secondsUntilSunrise(self):
        return self._secondsUntilSunEvent('sunrise')

    def _secondsUntilSunEvent(self, event):
        now = self.city.tz.localize(datetime.now())
        seconds = int(((self.city.sun(date=now, local=True))[event] - now).total_seconds())
        if seconds < 0:
            seconds = int((self.city.sun(date=now+timedelta(days=1), local=True)[event] - now).total_seconds())
        return seconds

if __name__ == '__main__':
    generator = SunEventGenerator('Chicago', 'http://localhost:8001', 255)
    try:
        print 'Running SunEventGenerator'
        print 'Making requests to:', generator.url, 'with value of', generator.value
        print 'Press Control-C to quit'
        while True:
            generator.setSunrise()
            generator.setSunset()
            for i in range(86400):
                time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
