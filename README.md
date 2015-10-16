# piLight
Simple Flask api to control PWM led's on the raspberry pi. 
Designed to be used with Thomas Sarlandie's [pi-blaster](https://github.com/sarfata/pi-blaster) to achieve full range PWM control on the pi's GPIO pins. 

## Usage
Only dependency is Flask. ```pip install flask```.

Various parameters can be edited in ```config.py```. Simply call ```python api.py``` to start the server. 

Simply make ```GET``` requests such as ```http://localhost:5000/setlights/255/255/255```. 
