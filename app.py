from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time, threading

# FROM VS CODE!!!

app = Flask(__name__)

channels = {
	'blue_lights': 2,
	'lamp_light': 3
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

# HIGH = off, LOW = on
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)

is_rave_mode = False
was_rave_mode = False

def check_rave_mode():
	print('check_rave_mode function start')
	global is_rave_mode
	global was_rave_mode
	global channels
	
	while True:
		if is_rave_mode == True:
			if was_rave_mode == False:
				# Rave mode initialized!
				was_rave_mode = True
				# start with one channel on, one channel off so that they alternate
				GPIO.output(channels['blue_lights'], GPIO.LOW)
				GPIO.output(channels['lamp_light'], GPIO.HIGH)
				continue

			for channel_id in channels.values():
				state = GPIO.input(channel_id)
				if state == True: # if channel is OFF (True = OFF)
					GPIO.output(channel_id, GPIO.LOW)
				else:
					GPIO.output(channel_id, GPIO.HIGH)

		else:
			if was_rave_mode == True:
				# rave_mode was just turned off:
				was_rave_mode = False
				# Turn off channels if any are left on:
				for channel_id in channels.values():
					GPIO.output(channel_id, GPIO.HIGH)

		time.sleep(0.07)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/turn_on')
def turn_on():
	channel_name = request.args['channel']
	channel_id = channels[channel_name]
	GPIO.output(channel_id, GPIO.LOW)
	return 'Channel {} set to ON'.format(channel_name)


@app.route('/turn_off')
def turn_off():
	channel_name = request.args['channel']
	channel_id = channels[channel_name]
	GPIO.output(channel_id, GPIO.HIGH)

	return 'Channel {} set to OFF'.format(channel_name)


@app.route('/toggle_rave')
def rave():
	global is_rave_mode
	is_rave_mode = not is_rave_mode
	return 'Denenenenenenenenenen!'


if __name__ == '__main__':
	rave_thread = threading.Thread(target = check_rave_mode)
	rave_thread.start()
	app.run(host='0.0.0.0')
