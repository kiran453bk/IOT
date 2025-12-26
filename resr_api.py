from flask import Flask, request, jsonify
import requests
import threading
import time

# ---------------------------
# Flask REST Server
# ---------------------------
app = Flask(__name__)

# In-memory IoT data store
sensor_data = {}


@app.route('/')
def home():
    return "Server running";

@app.route('/sensor/data', methods=['POST'])
def receive_data():
    data = request.json
    device_id = data.get("device_id")

    sensor_data[device_id] = {
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity")
    }

    return jsonify({"status": "Data received"}), 200


@app.route('/sensor/data/<device_id>', methods=['GET'])
def get_data(device_id):
    if device_id in sensor_data:
        return jsonify(sensor_data[device_id]), 200
    else:
        return jsonify({"error": "Device not found"}), 404


# ---------------------------
# Run Flask in Background
# ---------------------------
def run_server():
    app.run(port=5000, debug=False, use_reloader=False)


# ---------------------------
# IoT Sensor (Client)
# ---------------------------
def sensor_send_data():
    time.sleep(2)  # wait for server to start

    url = "http://127.0.0.1:5000/sensor/data"

    data = {
        "device_id": "sensor_001",
        "temperature": 29.2,
        "humidity": 68
    }

    response = requests.post(url, json=data)
    print("POST Response:", response.json())


# ---------------------------
# Data Consumer (Client)
# ---------------------------
def read_sensor_data():
    time.sleep(3)

    url = "http://127.0.0.1:5000/sensor/data/sensor_001"
    response = requests.get(url)

    print("GET Response:", response.json())


# ---------------------------
# Main
# ---------------------------
if __name__ == '__main__':

    # Start REST server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Simulate IoT sensor and client
    sensor_send_data()
    read_sensor_data()
