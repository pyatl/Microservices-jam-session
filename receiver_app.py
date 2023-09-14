from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        time_data = request.json.get('time')
        # Here you might want to save this time data somewhere, e.g., a database or a list
        # For this example, we'll just render it directly
        return render_template('index.html', times=[time_data])
    else:
        return render_template('index.html', times=["Not Found"])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
