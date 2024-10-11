from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoints to microservices
MICROSERVICE_1_URL = "http://localhost:5000"  # URL to product catalog microservice
MICROSERVICE_2_URL = "http://localhost:5001"  # URL to cart microservice

@app.route('/api/service1/<path:path>', methods=['GET', 'POST'])
def service1_proxy(path):
    url = f"{MICROSERVICE_1_URL}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json() if request.method == 'POST' else None,
        headers={key: value for key, value in request.headers if key != 'Host'}
    )
    return jsonify(response.json()), response.status_code






@app.route('/api/service2/<path:path>', methods=['GET', 'POST'])
def service2_proxy(path):
    url = f"{MICROSERVICE_2_URL}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json() if request.method == 'POST' else None,
        headers={key: value for key, value in request.headers if key != 'Host'}
    )
    return jsonify(response.json()), response.status_code






if __name__ == '__main__':
    app.run(port=5002)
