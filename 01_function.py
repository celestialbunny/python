from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1, num2):
	context = {'num1': num1, 'num2': num2}
	return render_template('multiply.html', **context)

@app.route('/capitalize')
def format_name():
	names = ( 'howdy', 'larry', 'alex' )
	return render_template('capitalize.html', names=names)

app.run(debug=True, port=8000, host='127.0.0.1')

@app.route('/mean/')
def mean():
	num1 = request.args.get('num1',1,type=int)
	num2 = request.args.get('num2',1,type=int)
	context = {'num1': num1, 'num2': num2}
	return render_template('mean.html', mean=context)