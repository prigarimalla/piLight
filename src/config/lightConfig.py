import json, sys
import drivers

driverModes = {driver.mode : driver for driver in drivers.LightDriver.LightDriver.__subclasses__()}

with open(sys.argv[1], 'r') as f:
    configData = json.load(f)

zones = [driverModes[entry["mode"]](
    description = entry["description"],
    pinout = entry["pinout"],
    calibration = entry["calibration"],
    mailbox = configData["mailbox"],
    fadelength = entry["fadelength"] if "fadelength" in entry else configData["fadelength"],
    fadesteps = entry["fadesteps"] if "fadesteps" in entry else configData["fadesteps"],
    gamma = entry["useGamma"] if "useGamma" in entry else configData["useGamma"],
    gammavals = [int(255*(i/255.0)**entry["gamma"]) for i in range(256)] if "gamma" in entry else [int(255*(i/255.0)**configData["gamma"]) for i in range(256)]
) for entry in configData["zones"]]

