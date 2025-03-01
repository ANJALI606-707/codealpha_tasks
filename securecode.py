from flask import Flask, request
from markupsafe import escape  # Correct import
import subprocess

app = Flask(__name__)

# Secure Command Execution
@app.route('/run', methods=['GET'])
def run_command():
    command = request.args.get('cmd')
    if command in ['ls', 'date', 'whoami']:  # Whitelist allowed commands
        result = subprocess.run([command], capture_output=True, text=True)
        return f"Output: {result.stdout}"
    else:
        return " Command not allowed!"

@app.route('/routes')
def list_routes():
    return str(app.url_map)

# Secure XSS Prevention
"""
@app.route('/greet', methods=['GET'])
def greet_user():
    user = request.args.get('name', 'Guest')  # ❌ Removed escape()
    return f"<h1>Welcome, {user}!</h1>"

"""
@app.route('/greet', methods=['GET'])
def greet_user():
    user = escape(request.args.get('name', 'Guest'))  # Escaping input
    return f"<h1>Welcome, {user}!</h1>"

# Disable Debug Mode for Production
if __name__ == '__main__':
    app.run(debug=False)  # Debug mode disabled