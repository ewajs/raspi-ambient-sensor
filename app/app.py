from flask import Flask, Response, render_template, url_for
import json
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_data():
	#conn = sqlite3.connect("/app/db/temphum.db")
	conn = sqlite3.connect("app/test.db")
	c = conn.cursor()
	c.execute("SELECT id, Temperature, Humidity, DATETIME(Timestamp,'localtime') FROM Ambient ORDER BY Timestamp DESC LIMIT 50")
	resp = json.dumps(list(c.fetchall()))
	conn.close()
	return Response(resp, mimetype='application/json')


@app.route("/report", methods=["GET"])
def report():
	#conn = sqlite3.connect("/app/db/temphum.db")
	conn = sqlite3.connect("app/test.db")
	c = conn.cursor()
	c.execute("""SELECT id, ReportName, 
		CASE
			WHEN Temperature = 1 THEN 'T'
			ELSE ''
		END Temperature,
		CASE
			WHEN Humidity = 1 THEN 'H'
			ELSE ''
		END Humidity,
		DATETIME(StartDate,'localtime'), DATETIME(StopDate,'localtime') FROM Report ORDER BY Timestamp DESC""")
	resp = list(c.fetchall())
	conn.close()
	# parse the the response into ID and Text
	data = []
	for item in resp:
		text = item[1] + ' - ' + item[2] + item[3] + ' - ' + item[4] + ' - ' + item[5]  
		data.append((item[0], text))
	return render_template("report.html", data=data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

