from flask import Flask, Response, render_template, url_for
import json
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_data():
	conn = sqlite3.connect("/app/db/temphum.db")
	c = conn.cursor()
	c.execute("SELECT id, Temperature, Humidity, DATETIME(Timestamp,'localtime') FROM Ambient ORDER BY Timestamp DESC")
	resp = json.dumps(list(c.fetchall()))
	conn.close()
	return Response(resp, mimetype='application/json')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

