
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DevOps Demo Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                text-align: center;
                padding-top: 100px;
            }
            .container {
                background: white;
                padding: 40px;
                margin: auto;
                width: 60%;
                border-radius: 12px;
                box-shadow: 0 4px 12px #ccc;
            }
            h1 { color: #2563eb; }
            h2 { color: green; }
            p { font-size: 18px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>DevOps Demo Application</h1>
            <h2>Application Running Successfully!</h2>
            <p>Developed using Python and Flask</p>
            <p>Environment: Local Development</p>
            <p>Status: Running</p>
        </div>
    </body>
    </html>
    """

@app.route("/status")
def status():
    return {
        "application": "DevOps Demo",
        "status": "Running",
        "environment": "Local"
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

