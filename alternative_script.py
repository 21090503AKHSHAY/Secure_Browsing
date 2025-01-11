from flask import Flask, request
import requests
import subprocess
import os
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        # Download the Debian package
        response = requests.get(url)
        if response.status_code == 200:
            # Generate a unique filename based on the URL
            file_name = hashlib.sha256(url.encode()).hexdigest() + '.deb'
            with open(file_name, 'wb') as f:
                f.write(response.content)
            
            # Install the Debian package using dpkg
            subprocess.run(['sudo', 'dpkg', '-i', file_name])
            
            return f"Downloading and installing package from {url}."
        else:
            return f"Failed to download {url}."
    else:
        return "No URL provided."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces
