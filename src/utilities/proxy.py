import http.server
import select
import ssl
import socketserver


class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_CONNECT(self):
        self.send_response(200, 'Connection Established')
        self.end_headers()
        self.server.connection = self.connection
        self._read_write()

    def _read_write(self):
        try:
            while not (self.server.client_closed or self.server.target_closed):
                r, w, e = select.select([self.connection, self.server.connection], [], [])
                if self.connection in r:
                    data = self.connection.recv(8192)
                    if not data:
                        self.server.client_closed = True
                        self.server.connection.close()
                        break
                    self.server.connection.sendall(data)
                if self.server.connection in r:
                    data = self.server.connection.recv(8192)
                    if not data:
                        self.server.target_closed = True
                        self.connection.close()
                        break
                    self.connection.sendall(data)
        finally:
            self.connection.close()
            self.server.connection.close()


class HTTPSProxyServer(socketserver.ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.client_closed = False
        self.target_closed = False

    def server_bind(self):
        self.socket = ssl.wrap_socket(
            self.socket,
            certfile='server.pem',  # Path to your server certificate
            keyfile='server.key',   # Path to your server private key
            server_side=True
        )
        super().server_bind()


if __name__ == '__main__':
    HOST, PORT = 'localhost', 8888
    server = HTTPSProxyServer((HOST, PORT), ProxyHandler)
    print(f'Starting HTTPS proxy server on {HOST}:{PORT}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Proxy server stopped')
        server.server_close()
