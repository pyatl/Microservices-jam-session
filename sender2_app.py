import requests
from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def send_time():
    time.sleep(2)  # 2 seconds delay
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requests.post('http://localhost:5000/', json={"time": current_time})
    return f"Time sent after delay: {current_time}"

if __name__ == "__main__":
    app.run(port=5002, debug=True)
