from flask import Flask,request 

app = Flask(__name__)
sCollec = []

@app.route('/',methods=["GET"])
def helloWorld():
	# http://localhost:5400/?clearStr
	if request.method=="GET" and "clearStr" in request.args:
		while len(sCollec):
			sCollec.pop()
		return "new initialisation"

	#http://localhost:5400/?concatStr
	if request.method=="GET" and "concatStr" in request.args:
		return ' '.join(sCollec)

	#http://localhost:5400/?addStr
	if request.method=="GET" and "addStr" in request.args: 
		sCollec.append(request.args.get('addStr'))
		return "added "+request.args.get('addStr')
	else:
		return """<title>DEVSNEST FLASK</title><body align="center">HOMEPAGE<br><br><br>use &nbsp;<code>http://127.0.0.1:5400/?addStr=STRING</code>&nbsp; to add STRING to your list <br><br> Then use <code>http://127.0.0.1:5400/?concatStr</code> &nbsp; to see all your string in one</body>"""



if __name__=="__main__":
	app.run(port=5400,debug=True)


## data = request.data()
# all get and post in json format is stored


#-------directly map to json
# data = request.json
# data[key]  = balue
# return jsonify(data)


# get from route
# @app.route('/greet/<string:user>',methods=["GET"])
# def greet(user):
# 	return "hello "+user