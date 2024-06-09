from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'apikey_apikey'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template('index.html', weather=weather)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
