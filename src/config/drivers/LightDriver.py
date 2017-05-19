class LightDriver(object):
    mode = 'generic'
    def setLights(self, color):
        raise NotImplementedError

class LightDriverError(Exception):
    def __str__(self):
        return 'Error while running driver'