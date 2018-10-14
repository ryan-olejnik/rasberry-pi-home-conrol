from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	print('HOME PAGE HIT!!!')
	return render_template('index.html')

@app.route('/settings')
def settings():
	return 'These are the settings!!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
