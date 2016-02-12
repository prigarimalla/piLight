from flask import Flask, url_for, Response, send_from_directory
import lightSetter

app = Flask(__name__, static_url_path='')
lightEngine = lightSetter.lightSetter()


@app.route('/setlights/<red>/<green>/<blue>')
def api_setLights(red, green, blue):
  try:
    lightEngine.setLights((int(red), int(green), int(blue)))
    return 'success'
  except ValueError as e:
    return 'failure'
    print e

@app.route('/setlights/<mono>')
def api_setLights_color(mono):
  lightEngine.setlights(mono)
  return 'success'

@app.route('/')
def webui():
  try:
    return send_from_directory('webui','index.html')
  except Exception as e:
    print e

@app.route('/js/sliders.js')
def webui_slider_js():
  return send_from_directory('webui/js','sliders.js')

@app.route('/css/sliders.css')
def webui_slider_css():
  return send_from_directory('webui/css','sliders.css')

if __name__ == '__main__':
  app.run(host='0.0.0.0')

