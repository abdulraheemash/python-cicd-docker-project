"""
Main Flask application
This is a simple API that demonstrates CI/CD best practices
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to CI/CD Demo!',
        'status': 'healthy'
    }), 200

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    """Greet a user"""
    if not name or len(name) < 2:
        return jsonify({'error': 'Invalid name'}), 400
    
    return jsonify({
        'greeting': f'Hello, {name}!',
        'status': 'success'
    }), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint (used by Kubernetes)"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
