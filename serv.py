#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File not found"
			self.send_response(404)

		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))


your_ip = '192.168.43.23'
httpd = HTTPServer((your_ip, 8081), Serv)
httpd.serve_forever()


