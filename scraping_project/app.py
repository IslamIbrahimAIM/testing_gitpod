from flask import Flask, jsonify
import json

app = Flask(__name__)

# Read the JSON file
with open('scraped_data.json') as f:
    data = json.load(f)

# Endpoint to view the details of the JSON file
@app.route('/', methods=['GET'])
def json_details():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4567)
