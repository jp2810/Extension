from flask import Flask,render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/iframe_div')
def iframe_div():
	return render_template('iframe_div.html')


if __name__== '__main__':
	app.run()

