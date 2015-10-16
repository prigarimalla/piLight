# piLight
Simple Flask api to control PWM LED's on the raspberry pi. 
Designed to be used with Thomas Sarlandie's [pi-blaster](https://github.com/sarfata/pi-blaster) to achieve full range PWM control on the pi's GPIO pins. 

## Usage

Upon installing pi-blaster and wiring up the LED's, configure the pin numbers, mailbox locations, and any other desired parameters in ```config.py```

Only dependency is Flask. ```pip install flask```.Simply call ```python api.py``` to start the server. Just make ```GET``` requests such as ```http://localhost:5000/setlights/255/255/255```. 
