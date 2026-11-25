import os
import sys
import time
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
last_ping = time.time()
connected = False


class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        global last_ping, connected
        if self.path.startswith("/ping"):
            last_ping = time.time()
            connected = True
            self.send_response(204)
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format, *args):
        pass


def watchdog():
    while True:
        time.sleep(2)
        if connected and (time.time() - last_ping > 6):
            os._exit(0)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 0), QuietHandler)
    port = server.server_address[1]
    threading.Thread(target=watchdog, daemon=True).start()
    webbrowser.open(f"http://127.0.0.1:{port}/index.html")
    server.serve_forever()