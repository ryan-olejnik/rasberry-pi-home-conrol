from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time, threading

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# HIGH = off, LOW = on
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)

is_rave_mode_2 = False
was_rave_mode_2 = False

def check_rave_mode():
	global was_rave_mode_2
	while True:
		if is_rave_mode_2 == True:
			was_rave_mode_2 = True
			print('Rave mode!')
			state = GPIO.input(2)
			if state == True:
				GPIO.output(2, GPIO.LOW)
			else:
				GPIO.output(2, GPIO.HIGH)
		else:
			if was_rave_mode_2:
				GPIO.output(2, GPIO.HIGH)
				was_rave_mode_2 = False
		time.sleep(0.2)


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
	global is_rave_mode_2
	is_rave_mode_2 = False
	GPIO.output(channel,GPIO.HIGH)
	return 'Channel {} set to OFF'.format(channel)


@app.route('/toggle')
def toggle():
	channel = int(request.args['channel'])

	state = GPIO.input(channel)
	if state == True:
		GPIO.output(channel, GPIO.LOW)
	else:
		GPIO.output(channel, GPIO.HIGH)
	return 'Pin was toggled'

@app.route('/toggle_rave')
def rave():
	channel = int(request.args['channel'])
	global is_rave_mode_2
	is_rave_mode_2 = not is_rave_mode_2
	return 'Denenenenenenenenenen!'

if __name__ == '__main__':
	thread = threading.Thread(target = check_rave_mode)
	thread.start()
	app.run(host='0.0.0.0')
