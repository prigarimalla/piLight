import config, time

class lightSetter(object):
	def __init__(self, pins=[config.redpin, config.greenpin, config.bluepin], 
		mailbox=config.mailboxloc, 
		fadelength=config.fadelength, 
		fadesteps=config.fadesteps, 
		gammavals=config.gammavals, 
		gamma=config.gamma, 
		colors=config.colors, 
		calibration=[config.redcal, config.greencal, config.bluecal]):
		self.pins = pins
		self.mailbox = mailbox
		self.curcolor = [0,0,0]
		self.fadelength = fadelength
		self.fadesteps = fadesteps
		self.gammavals = gammavals
		self.gamma = gamma
		self.colors = colors
		self.calibration = calibration
		self._sendData((0,0,0))

	def setLights(self, color):
		if isinstance(color, str):
			try:
				self._fade(self.colors[color])
			except KeyError:
				print 'Failure - Invalid color name'
				print color
			except Exception as e: 
				print 'Failure - Fatal Error'
				print e
		else:
			try:
				self._fade(color)
			except ValueError:
				print 'Failure - Invalid color'
				print color
			except Exception as e: 
				print 'Failure - Fatal Error'
				print e

	def _fade(self, color):
		fadeColor = [float(v) for v in color]
		delta = [(f-c)/self.fadesteps for f,c in zip(fadeColor, [float(i) for i in self.curcolor])]
		startcolor = self.curcolor
		for step in range(1, self.fadesteps+1):
			self._sendData([(d*step)+s for d,s in zip(delta, startcolor)])
			time.sleep(self.fadelength)
	
	def _sendData(self, color):
		with open(self.mailbox, 'a') as m:
			if self.gamma:
				m.write(self.pins[0]+'='+str(self.calibration[0]*(self.gammavals[int(color[0])]/255.0))+'\n' + 
					self.pins[1]+'='+str(self.calibration[1]*(self.gammavals[int(color[1])]/255.0))+'\n' + 
					self.pins[2]+'='+str(self.calibration[2]*(self.gammavals[int(color[2])]/255.0))+'\n')
			else:
				m.write(self.pins[0]+'='+str(self.calibration[0]*(color[0]/255.0))+'\n' + 
					self.pins[1]+'='+str(self.calibration[1]*(color[1]/255.0))+'\n' + 
					self.pins[2]+'='+str(self.calibration[2]*(color[2]/255.0))+'\n')
		self.curcolor = [int(i) for i in color]

if __name__ == '__main__':
	s = lightSetter()
	s.setLights('WHITE')
	s.setLights('DIM')
	s.setLights('WARM')
	s.setLights('WHITE')
	s.setLights('OFF')