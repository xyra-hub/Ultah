import http.server
import socketserver
import webbrowser

PORT = 8000
file_name = "ulang_tahun.html"

print(f"Server berjalan di http://localhost:{PORT}/{file_name}")
webbrowser.open(f"http://localhost:{PORT}/{file_name}")

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()