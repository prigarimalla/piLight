import time
from LightDriver import LightDriver, LightDriverError

class MonoDriver(LightDriver):
    mode = 'mono'
    def __init__(self, pinout, description, mailbox, fadelength, fadesteps, gammavals, gamma, calibration):
        self.description = description
        self.pinout = pinout
        self.mailbox = mailbox
        self.fadelength = fadelength
        self.fadesteps = fadesteps
        self.gammavals = gammavals
        self.gamma = gamma
        self.calibration = calibration
        self.curcolor = 0
        self._sendData(self.curcolor)

    def setLights(self, color):
        try:
            if isinstance(color, int):
                self._fade(color)
            elif isinstance(color, tuple):
                self._fade(color[0])
        except:
            raise LightDriverError

    def _fade(self, color):
        fadeColor = float(color)
        delta = (fadeColor - self.curcolor)/self.fadesteps
        startColor = self.curcolor
        for step in range(1, self.fadesteps+1):
            self._sendData((delta*step)+startColor)
            time.sleep(self.fadelength)

    def _sendData(self, color):
        with open(self.mailbox, 'a') as m:
            if self.gamma:
                m.write(self.pinout+'='+str(self.calibration*(self.gammavals[int(color)/255.0]))+'\n')
            else:
                m.write(self.pinout+'='+str(self.calibration*(int(color)/255.0))+'\n')
        self.curcolor = int(color)