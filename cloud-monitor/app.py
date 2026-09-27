from flask import Flask, render_template
import psutil
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage("/").percent,
        host=socket.gethostname(),
        status="ONLINE"
    )

app.run(host="0.0.0.0", port=5000)