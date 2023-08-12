import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or Memory Utilization detected. Please scale up"
    else:
        message = ""  # No message when conditions are not met

    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)

@app.route("/metric_data")
def metric_data():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    data = {"cpu": cpu_percent, "memory": mem_percent}
    return jsonify(data)  # Use jsonify to serialize the data as JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

