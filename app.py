from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(2,GPIO.OUT)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/turn_on')
def turn_on():
	GPIO.output(2,GPIO.HIGH)
	return 'Pin set to HIGH'

@app.route('/turn_off')
def turn_off():
        GPIO.output(2,GPIO.LOW)
        return 'Pin set to LOW'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
