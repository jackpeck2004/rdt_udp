import socket

ACK = "ACK"
NAK = "NAK"

UDP_SRC_IP, UDP_SRC_PORT = "127.0.0.1", 5005
UDP_DEST_IP, UDP_DEST_PORT = "127.0.0.1", 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_SRC_IP, UDP_SRC_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Received: ", data.decode())
    if data.decode() == "HELLO":
        sock.sendto(ACK.encode(), (UDP_DEST_IP, UDP_DEST_PORT))
    else:
        sock.sendto(NAK.encode(), (UDP_DEST_IP, UDP_DEST_PORT))

