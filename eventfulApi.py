from config.eventConfig import pollingInterval
from config.events.sunEventGenerator import sunEventGenerator as eventGenerator
import api, thread, time

lightEngine = api.lightEngine
generator = eventGenerator()

def eventThread():
	while True:
		time.sleep(pollingInterval)
		color = generator.getEvent()
		if color != (-1,-1,-1):
			lightEngine.setLights(color)

if __name__ == '__main__':
	thread.start_new_thread(eventThread, ())
	api.app.run(host='0.0.0.0')
