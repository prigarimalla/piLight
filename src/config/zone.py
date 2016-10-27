class Zone(object):
    def __init__(self, mode, pinout, description):
        self.description = description
        self.mode = mode
        if self.mode is not 'rgb' and self.mode is not 'mono':
            raise BadZoneException
        if self.mode is 'rgb':
            if not isinstance(pinout, tuple) or not len(pinout) is 3:
                raise BadZoneException
            self.pinout = [str(pin) for pin in pinout]
        if self.mode is 'mono':
            if not isinstance(pinout, int):
                raise BadZoneException
            self.pinout = str(pinout)

class BadZoneException(Exception):
    def __str__(self):
        return 'Bad Zone Definition'