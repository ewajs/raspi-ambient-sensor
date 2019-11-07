import csv
from flask import Flask, jsonify, make_response, Response, render_template, request, url_for
import io
import json
import sqlite3

app = Flask(__name__)

def connect():
	#conn = sqlite3.connect("/app/db/temphum.db") # Production DB
	conn = sqlite3.connect("app/test.db") # For testing purposes
	return conn

def get_report_data(conn):
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
	# parse the the response into ID and Text
	data = []
	for item in resp:
		text = item[1] + ' - ' + item[2] + item[3] + ' - ' + item[4] + ' - ' + item[5]  
		data.append((item[0], text))
	return data

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_data():
	conn = connect()
	c = conn.cursor()
	c.execute("SELECT id, Temperature, Humidity, DATETIME(Timestamp,'localtime') FROM Ambient ORDER BY Timestamp DESC LIMIT 50")
	resp = json.dumps(list(c.fetchall()))
	conn.close()
	return Response(resp, mimetype='application/json')


@app.route("/report", methods=["GET", "POST"])
def report():
	if request.method == 'GET':
		conn = connect()
		data = get_report_data(conn)
		conn.close()
		return render_template("report.html", data=data, success=None)
	elif request.method == 'POST':
		conn = connect()
		c = conn.cursor()
		c.execute("SELECT COUNT(id) FROM Ambient WHERE DATETIME(Timestamp,'localtime') BETWEEN ? AND ?", (request.form["StartDate"], request.form["StopDate"]))
		entries = c.fetchall()[0][0]
		success = entries != 0 # If no entries, cannot create the report.
		if success:
			c = conn.cursor()
			# Temperature and Humidity are fetched differently because they might not be defined.
			temp = 1 if 'Temperature' in request.form else 0
			hum = 1 if 'Humidity' in request.form else 0 
			c.execute('INSERT INTO Report (ReportName, Temperature, Humidity, StartDate, StopDate) VALUES (?, ?, ?, ?, ?);',
			(request.form["ReportName"], temp, hum, request.form["StartDate"], request.form["StopDate"]))
			conn.commit()
		data = get_report_data(conn)
		conn.close()
		return render_template("report.html", data=data, success=success)

@app.route("/show_report", methods=["GET"])
def show_report():
	if request.method == 'GET':
		conn = connect()
		c = conn.cursor()
		rid = request.args["reportid"]
		c.execute("""SELECT * FROM Ambient WHERE Timestamp 
		BETWEEN (SELECT StartDate FROM Report WHERE id = ?) AND (SELECT StopDate FROM Report WHERE id = ?) 
		ORDER BY Timestamp DESC """, (rid, rid))
		data = list(c.fetchall())
		c = conn.cursor()
		c.execute("SELECT ReportName, Temperature, Humidity FROM Report WHERE id = ?", (rid, ))
		report_data = list(c.fetchall())[0]
		conn.close()
		return render_template("show_report.html", data=data, report_data=report_data)

@app.route('/export', methods=["GET"])
def export_data():
	if request.method == 'GET':
		si = io.StringIO()
		cw = csv.writer(si)
		conn = connect()
		c = conn.cursor()
		rid = request.args["reportid"]
		c.execute("""SELECT Timestamp, Temperature, Humidity FROM Ambient WHERE Timestamp 
		BETWEEN (SELECT StartDate FROM Report WHERE id = ?) AND (SELECT StopDate FROM Report WHERE id = ?) 
		ORDER BY Timestamp DESC """, (rid, rid))
		# Add the headers
		cw.writerow(["Fecha y Hora", "Temperatura", "Humedad"])
		# Then the data
		cw.writerows(list(c.fetchall()))
		output = make_response(si.getvalue())
		output.headers["Content-Disposition"] = "attachment; filename=export.csv"
		output.headers["Content-type"] = "text/csv"
		return output


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

