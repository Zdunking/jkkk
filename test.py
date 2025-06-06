print("Hello, World!")

# http 静态服务器
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class RedirectHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not os.path.exists(self.translate_path(self.path)) or os.path.isdir(self.translate_path(self.path)):
            self.path = '/train.html'
        return super().do_GET()
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RedirectHandler)
    # 挂载当前目录
    
    # 重定向到/train.html
    
    httpd.serve_forever()

if __name__ == "__main__":
    main()