from flask import Flask, jsonify
from latency_parser import extract_latency

app = Flask(__name__)

@app.route('/latency')
def get_latency():
    latency = extract_latency('latest.pcap')
    return jsonify({"latency_ms": latency * 1000})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

