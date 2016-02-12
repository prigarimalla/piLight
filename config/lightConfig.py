#Configuration for lightSetter

#RGB or MONO mode
mode='rgb'
#mode='mono'

#GPIO pin numbers for leds. 
monopin='23'
redpin='23'
greenpin='18'
bluepin='24'

#Location of mailbox. Default for pi-blaster is /dev/pi-blaster.
#Can change for testing purposes. 
#mailboxloc='/dev/pi-blaster'
mailboxloc='test'

#Parameters for fades. Duration in seconds for sleep between steps and number of steps.
fadelength=0.01
fadesteps=20

#List of pre-defined colors
colors={}
colors['WHITE']=(255, 255, 255)
colors['RED']=(255, 0, 0)
colors['GREEN']=(0, 255, 0)
colors['BLUE']=(0, 0, 255)
colors['OFF']=(0, 0, 0)
colors['WARM']=(255, 70, 0)
colors['DIM']=(140, 140, 140)

#List of gamma corrected values
gammavals=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 
7, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 36, 38, 39, 41, 43, 44, 46, 48, 50, 
52, 54, 56, 58, 60, 62, 64, 67, 69, 71, 74, 76, 79, 81, 84, 87, 89, 92, 95, 98, 100, 103, 
106, 109, 112, 115, 118, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 156, 
159, 162, 165, 167, 170, 173, 175, 178, 180, 183, 185, 187, 190, 192, 194, 196, 198, 200, 
202, 204, 206, 208, 210, 211, 213, 215, 216, 218, 219, 221, 222, 223, 225, 226, 227, 228, 
229, 230, 231, 232, 233, 234, 235, 236, 237, 237, 238, 239, 239, 240, 241, 241, 242, 242, 
243, 243, 244, 244, 245, 245, 246, 246, 246, 247, 247, 247, 248, 248, 248, 249, 249, 249, 
249, 250, 250, 250, 250, 250, 251, 251, 251, 251, 251, 251, 252, 252, 252, 252, 252, 252, 
252, 252, 252, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 253, 
254, 254, 254, 254, 254, 254, 254, 255, 255]

#Whether or not to use gamma correction.
gamma=False

#Calibration of the RGB channels. Each value is a percentage [0,1] of maximum.
redcal=1.0
greencal=1.0
bluecal=1.0

