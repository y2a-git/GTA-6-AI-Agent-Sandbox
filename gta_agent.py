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

        if self.path.split("?", 1)[0] in ("/", "/index.html"):
            index_path = os.path.join(BASE_DIR, "index.html")
            try:
                with open(index_path, "r", encoding="utf-8") as index_file:
                    html = index_file.read()
                marker = "<script src=\"/neon-coast.js\"></script>"
                if marker not in html:
                    html = html.replace("</head>", marker + "\n</head>", 1)
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
                return
            except OSError as exc:
                self.send_error(500, "Unable to load Neon Coast: %s" % exc)
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
    webbrowser.open("http://127.0.0.1:%d/index.html" % port)
    server.serve_forever()
