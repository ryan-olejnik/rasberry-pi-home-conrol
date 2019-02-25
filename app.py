from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time, threading
from datetime import datetime

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

GPIO.ON = GPIO.LOW
GPIO.OFF = GPIO.HIGH

# initialize channels to OFF:
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.output(2, GPIO.OFF)
GPIO.output(3, GPIO.OFF)

is_rave_mode = False
was_rave_mode = False

CHANNELS = {
	'blue_lights': 2,
	'lamp_light': 3
}

EVENTS = [
	{
		'name': 'Morning alarm: Turn ON blue lights',
		'channel_id': CHANNELS['blue_lights'],
		'set_to': GPIO.ON,
		'weekdays': [0, 1, 2, 3, 4],
		'hour': 22,
		'minute': 11
	},
	{
		'name': 'Morning alarm: Turn off blue lights',
		'channel_id': CHANNELS['blue_lights'],
		'set_to': GPIO.OFF,
		'weekdays': [0, 1, 2, 3, 4],
		'hour': 22,
		'minute': 12
	},
]

def start_rave_thread():
	print('start_rave_thread function start')
	global is_rave_mode
	global was_rave_mode
	global CHANNELS
	
	while True:
		if is_rave_mode == True:
			if was_rave_mode == False:
				# Rave mode initialized!
				was_rave_mode = True
				# start with one channel on, one channel off so that they alternate
				GPIO.output(CHANNELS['blue_lights'], GPIO.LOW)
				GPIO.output(CHANNELS['lamp_light'], GPIO.HIGH)
				continue

			for channel_id in CHANNELS.values():
				state = GPIO.input(channel_id)
				if state == True: # if channel is OFF (True = OFF)
					GPIO.output(channel_id, GPIO.LOW)
				else:
					GPIO.output(channel_id, GPIO.HIGH)

		else:
			if was_rave_mode == True:
				# rave_mode was just turned off:
				was_rave_mode = False
				# Turn off CHANNELS if any are left on:
				for channel_id in CHANNELS.values():
					GPIO.output(channel_id, GPIO.HIGH)

		time.sleep(0.07)


def start_alarm_thread():
	while True:
		now = datetime.now()
		print('checking for EVENTS at time: ', now)
		for event in EVENTS:
			if now.hour == event['hour'] and now.minute == event['minute'] and now.weekday() in event['weekdays']:
				print('EVENT: ', event['name'])
				GPIO.output(event['channel_id'], event['set_to'])

		time.sleep(5)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/turn_on')
def turn_on():
	channel_name = request.args['channel']
	channel_id = CHANNELS[channel_name]
	GPIO.output(channel_id, GPIO.ON)
	return 'Channel {} set to ON'.format(channel_name)


@app.route('/turn_off')
def turn_off():
	channel_name = request.args['channel']
	channel_id = CHANNELS[channel_name]
	GPIO.output(channel_id, GPIO.OFF)

	return 'Channel {} set to OFF'.format(channel_name)


@app.route('/toggle_rave')
def rave():
	global is_rave_mode
	is_rave_mode = not is_rave_mode
	return 'Denenenenenenenenenen!'


if __name__ == '__main__':
	rave_thread = threading.Thread(target = start_rave_thread)
	alarm_thread = threading.Thread(target = start_alarm_thread)
	rave_thread.start()
	alarm_thread.start()
	app.run(host='0.0.0.0')
