from flask import Flask, request
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        webbrowser.open_new_tab(url)
        return f"Opening {url} in browser."
    else:
        return "No URL provided."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Change the host and port as needed
