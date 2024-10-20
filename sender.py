import socket

MESSAGE = "HELLO"
UDP_SRC_IP, UDP_SRC_PORT = "127.0.0.1", 5000
UDP_DEST_IP, UDP_DEST_PORT = "127.0.0.1", 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_SRC_IP, UDP_SRC_PORT))

def make_pkt(data: str) -> bytes:
    return bytes(data, 'utf-8')

def udp_send(pkt: bytes):
    sock.sendto(pkt, (UDP_DEST_IP, UDP_DEST_PORT))

def rdt_send(data: str):
    pkt = make_pkt(data)
    udp_send(pkt)


def main():
    rdt_send("HELLO")
    ok: bool = False
    while not ok:
        pkt, _ = sock.recvfrom(1024)
        print(pkt)
        ok = True


if __name__ == "__main__":
    main()

