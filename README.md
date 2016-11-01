# piLight 2
piLight is a suite for controlling LED strips with the Raspberry Pi. It consists of a RESTful API, a Web Interface, and supports event generators to control the lights in response to events (these are in essence just their own microservices). 

The API is designed to be used with Thomas Sarlandie's [pi-blaster](https://github.com/sarfata/pi-blaster). The two together set the specified zones' pins to a PWM value. There are a variety of circuits to interface the PWM signal with the lights themselves. 

The current version of the web interface is live at http://prigarimalla.github.io/piLight/webui/ (click on the gear icon in the top right corner to set the URL for your API). 

## Usage
First, install [pi-blaster](https://github.com/sarfata/pi-blaster) and use pip to install all the python dependencies (`pip install -r requirements.txt`). Then configire `lightConfig.py`. Most of values can remain the same, the only part that needs configuration is `zones`. Each comma separated entry in the array goes as follows:

For an RGB zone:
    
        Zone('rgb', (<redPin>, <greenPin>, <bluePin>), '<description>')
        
For a mono zone:

        Zone('mono', <pin>, '<description>')


To simply test the API and have the output be written to a file, leave the line

        mailboxloc='test'
uncommented. This will write the output to a file called `test`. 

To actually have the API control the lights, uncomment the line

        mailboxloc='/dev/pi-blaster'
        
and comment out any other assignments to `mailboxloc`.
