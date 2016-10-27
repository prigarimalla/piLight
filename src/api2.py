from flask import Flask, request, Response
import httplib, json
from LightManager import LightManager

app = Flask(__name__, static_url_path='')
manager = LightManager()

def getColor():
    if 'red' in request.args and 'green' in request.args and 'blue' in request.args:
            color = (int(request.args.get('red')), int(request.args.get('green')), int(request.args.get('blue')))
    elif 'mono' in request.args:
        color = int(request.args.get('mono'))
    else:
        raise Exception
    return color

def getZone():
    if 'zone' in request.args:
        return request.args.get('zone')
    else:
        return None

@app.route('/setLights/')
def apiSetLights():
    try:
        color = getColor()
        zone = getZone()
        manager.setLights(color, zone)
        return Response(status=httplib.NO_CONTENT)
    except:
        return Response(status=httplib.BAD_REQUEST)

@app.route('/setEvent/')
def apiSetEvent():
    try:
        color = getColor()
        zone = getZone()
        delay = int(request.args.get('delay'))
        eventId = manager.setEvent(delay, color, zone)
        body = json.dumps({'eventId': eventId})
        return Response(response=body, status=httplib.OK)
    except:
        return Response(status=httplib.BAD_REQUEST)

@app.route('/cancelEvent/')
def apiCancelEvent():
    try:
        eventId = request.args.get('eventId')
        manager.cancelEvent(eventId)
        return Response(status=httplib.NO_CONTENT)
    except:
       return Response(status=httplib.BAD_REQUEST)

@app.route('/getZoneInfo/')
def apiGetZoneInfo():
    try:
        body = json.dumps(manager.getZoneInfo())
        return Response(response=body, status=httplib.OK)
    except:
        return Response(status=httplib.INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8001)