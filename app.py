from flask import Flask, jsonify, render_template, request
import pdb
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=str)
    
    print "hello";
    print c;
    return jsonify(result=a+b)
@app.route('/')
def index():
    return render_template('popup1.html')
    
if __name__=="__main__":
    app.run(debug=True);
