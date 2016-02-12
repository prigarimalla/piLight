import config.lightConfig as config
import time

class lightSetter(object):
	def __init__(self, pins=[config.redpin, config.greenpin, config.bluepin], 
		monopin=config.monopin,
		mailbox=config.mailboxloc, 
		fadelength=config.fadelength, 
		fadesteps=config.fadesteps, 
		gammavals=config.gammavals, 
		gamma=config.gamma, 
		colors=config.colors, 
		calibration=[config.redcal, config.greencal, config.bluecal], 
		mode=config.mode):
		self.pins = pins
		self.monopin = monopin
		self.mailbox = mailbox
		self.fadelength = fadelength
		self.fadesteps = fadesteps
		self.gammavals = gammavals
		self.gamma = gamma
		self.colors = colors
		self.calibration = calibration
		self.mode = mode
		self.curcolor = (0,0,0) if self.mode is True else 0
		self._sendData(self.curcolor)

	def setLights(self, color):
		if self.mode == 'mono' and isinstance(color, int):
			self._changeLights(color)
		if self.mode == 'mono' and isinstance(color, tuple):
			self._changeLights(color[0])
		if self.mode == 'rgb' and isinstance(color, int):
			self._changeLights((color,color,color))
		if self.mode == 'rgb' and isinstance(color, tuple):
			self._changeLights(color)

	def _changeLights(self, color):
		try:
			self._fade(color)
		except KeyError:
			print 'Failure - Invalid color'
			print color
		except Exception as e: 
			print 'Failure - Fatal Error'
			print e

	def _fade(self, color):
		if self.mode == 'mono':
			fadeColor = float(color)
			delta = (fadeColor - self.curcolor)/self.fadesteps
			startcolor = self.curcolor
			for step in range(1, self.fadesteps+1):
				self._sendData((delta*step)+startcolor)
				time.sleep(self.fadelength)
		else:
			fadeColor = [float(v) for v in color]
			delta = [(f-c)/self.fadesteps for f,c in zip(fadeColor, [float(i) for i in self.curcolor])]
			startcolor = self.curcolor
			for step in range(1, self.fadesteps+1):
				self._sendData([(d*step)+s for d,s in zip(delta, startcolor)])
				time.sleep(self.fadelength)
	
	def _sendData(self, color):
		if self.mode == 'mono':
			with open(self.mailbox, 'a') as m:
				if self.gamma:
					m.write(self.monopin+'='+str(self.gammavals[int(color/255.0)]))
				else:
					m.write(self.monopin+'='+str(int(color/255.0)))
			self.curcolor = int(color)
		else:
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
