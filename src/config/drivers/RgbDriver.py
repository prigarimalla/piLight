import time
from LightDriver import LightDriver, LightDriverError

class RgbDriver(LightDriver):
    mode = 'rgb'
    def __init__(self, pinout, description, mailbox, fadelength, fadesteps, gammavals, gamma, calibration):
        self.description = description
        self.pinout = pinout
        self.mailbox = mailbox
        self.fadelength = fadelength
        self.fadesteps = fadesteps
        self.gammavals = gammavals
        self.gamma = gamma
        self.calibration = calibration
        self.curcolor = (0,0,0)
        self._sendData(self.curcolor)

    def setLights(self, color):
        try:
            if isinstance(color, int):
                self._fade((color,color,color))
            if isinstance(color, tuple):
                self._fade(color)
        except:
            raise LightDriverError

    def _fade(self, color):
        fadeColor = [float(v) for v in color]
        delta = [(f-c)/self.fadesteps for f,c in zip(fadeColor, [float(i) for i in self.curcolor])]
        startColor = self.curcolor
        for step in range(1, self.fadesteps+1):
            self._sendData([(d*step)+s for d,s in zip(delta, startColor)])
            time.sleep(self.fadelength)

    def _sendData(self, color):
        with open(self.mailbox, 'a') as m:
            if self.gamma:
                m.write(self.pinout[0] + '=' + str(self.calibration[0] * (self.gammavals[int(color[0])] / 255.0)) + '\n' +
                        self.pinout[1] + '=' + str(self.calibration[1] * (self.gammavals[int(color[1])] / 255.0)) + '\n' +
                        self.pinout[2] + '=' + str(self.calibration[2] * (self.gammavals[int(color[2])] / 255.0)) + '\n')
            else:
                m.write(self.pinout[0] + '=' + str(self.calibration[0] * (color[0] / 255.0)) + '\n' +
                        self.pinout[1] + '=' + str(self.calibration[1] * (color[1] / 255.0)) + '\n' +
                        self.pinout[2] + '=' + str(self.calibration[2] * (color[2] / 255.0)) + '\n')
        self.curcolor = [int(i) for i in color]
