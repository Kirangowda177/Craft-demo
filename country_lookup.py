from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/health')
def health():
    return 'Service is healthy'

@app.route('/diag')
def diag():
    api_status = requests.get('https://www.travel-advisory.info/api').json()
    return jsonify(api_status)

@app.route('/convert/<country_name>')
def convert(country_name):
    # Your country code conversion logic here
    # Assuming you have a function convert_country_code(country_name) in your script
    country_code = convert_country_code(country_name)
    return jsonify({'country_code': country_code})

if __name__ == '__main__':
    app.run(debug=True)