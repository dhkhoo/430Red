# File upload can exfiltrate files on the network.

# This script should serve files in the local folder running an HTTP server.

export LPORT=8888
python -c 'import sys; from os import environ as e
if sys.version_info.major == 3: import http.server as s, socketserver as ss
else: import SimpleHTTPServer as s, SocketServer as ss
ss.TCPServer(("", int(e["LPORT"])), s.SimpleHTTPRequestHandler).serve_forever()'
