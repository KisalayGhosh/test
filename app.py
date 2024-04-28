from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


API_KEY = '8ef18304598dc1f48f9ab25916f8d7bc'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'rainfall': data.get('rain', {}).get('1h', 0)  
        }
        return jsonify(weather)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
