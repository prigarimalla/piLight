from flask import Flask, request, Response
import httplib, json
from LightScheduler import LightScheduler
app = Flask(__name__, static_url_path='')
scheduler = LightScheduler()

def getColor():
    if 'red' in request.args and 'green' in request.args and 'blue' in request.args:
            color = (int(request.args.get('red')), int(request.args.get('green')), int(request.args.get('blue')))
    elif 'mono' in request.args:
        color = int(request.args.get('mono'))
    else:
        raise Exception
    return color

@app.route('/setLights/')
def apiSetLights():
    try:
        color = getColor()
        scheduler.setLights(color)
        return Response(status=httplib.NO_CONTENT)
    except:
        return Response(status=httplib.BAD_REQUEST)

@app.route('/setEvent/')
def apiSetEvent():
    try:
        color = getColor()
        delay = int(request.args.get('delay'))
        eventId = scheduler.setEvent(delay, color)
        body = json.dumps({'eventId': eventId})
        return Response(response=body, status=httplib.OK)
    except:
        return Response(status=httplib.BAD_REQUEST)

@app.route('/cancelEvent/')
def apiCancelEvent():
    try:
        eventId = request.args.get('eventId')
        scheduler.cancelEvent(eventId)
        return Response(status=httplib.NO_CONTENT)
    except:
       return Response(status=httplib.BAD_REQUEST)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8001)