from flask import Flask, render_template, request

app = Flask(__name__)

# A global list to store times
received_times = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        time_data = request.json.get('time')
        received_times.append(time_data)  # Save received time
        print("Received data:", request.json)  # Debug print statement
        return render_template('index.html', times=received_times)
    else:
        if not received_times:
            return render_template('index.html', times=["Not Found"])
        else:
            return render_template('index.html', times=received_times)
        
def something(item1=int, item2=int) -> int:
    thing = int(input(item1, item2))
    return int(thing)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
