from flask import Flask, jsonify, render_template, request,json
import pdb
app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    
    print "hello";
    b=[1,2,3]
    c=["jayesh","pawar"]
    txt='{"result" : '
    txt += json.dumps(c)
    txt += "}"
    print txt
    return txt
   #return '{"result":["jayesh","pawar"]}' ...working

@app.route('/')
def index():
    return render_template('popup.html')
    
if __name__=="__main__":
    app.run(debug=True);