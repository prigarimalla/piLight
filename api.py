from flask import Flask, url_for, Response
import lightSetter

app = Flask(__name__)
lightEngine = lightSetter.lightSetter()

@app.route('/setlights/<red>/<green>/<blue>')
def api_setLights(red, green, blue):
  try:
    lightEngine.setLights((int(red), int(green), int(blue)))
    return 'success'
  except ValueError as e:
    return 'failure'
    print e

@app.route('/setlights/<color>')
def api_setLights_color(color):
  lightEngine.setlights(color)
  return success

if __name__ == '__main__':
  app.run(host='0.0.0.0')

