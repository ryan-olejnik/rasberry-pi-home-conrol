from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# HIGH = off, LOW = on
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/turn_on')
def turn_on():
	channel = int(request.args['channel'])
	GPIO.output(channel,GPIO.LOW)
	return 'Channel {} set to ON'.format(channel)


@app.route('/turn_off')
def turn_off():
        channel = int(request.args['channel'])
        GPIO.output(channel,GPIO.HIGH)
        return 'Channel {} set to OFF'.format(channel)


@app.route('/toggle')
def toggle():
	channel = int(request.args['channel'])

	state = state = GPIO.input(channel)
	if state == True:
		GPIO.output(channel, GPIO.LOW)
	else:
		GPIO.output(channel, GPIO.HIGH)
	return 'Pin was toggled'

@app.route('/toggle_rave')
def rave():
	channel = int(request.args['channel'])
	while True:
		GPIO.output(channel, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(channel, GPIO.LOW)
		time.sleep(0.1)
	return 'Denenenenenenenenenen!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
