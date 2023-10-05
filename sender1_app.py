import requests
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def send_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requests.post('http://127.0.0.1:5000/', json={"time": current_time})
    return f"Time sent: {current_time}"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
