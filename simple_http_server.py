#!/usr/bin/python
import socket
import re

def create_socket(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((ip, port))
	print 'starting up on %s port %d' % (ip, port)
	return sock

def get_uri(request):
	uri = re.findall(r"GET .* HTTP", request);
	if len(uri) > 0:
		uri = uri[0][4:-5]
	else:
		uri = ""
	return uri

def response(conn, mime, content):
	res =       "HTTP/1.0 200 OK\n"
	res = res + "Content-length: %d\n" % len(content)
	res = res + "Content-Type: %s\n\n" % mime
	res = res + content
	conn.sendall(res)

res="""
<html>
<head>
<title>Success</title>
</head>
<body>
Boo!
</body>
</html>
"""

sock = create_socket('127.0.0.1', 15000)
sock.listen(10)

while True:
	conn, clnt_addr = sock.accept()
	try:
		request = conn.recv(1024)
		print get_uri(request)
		response(conn, "text/html", res);
	finally:
		conn.close()