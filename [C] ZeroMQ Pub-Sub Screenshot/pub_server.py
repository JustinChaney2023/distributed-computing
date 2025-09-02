import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]  # string is fine

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind(f"tcp://*:{port}")

# Give subscribers time to connect (slow joiner problem).
time.sleep(0.5)

while True:
    topic = random.randrange(9999, 10005)   # 9999..10004 inclusive
    messagedata = random.randrange(1, 215) - 80
    payload = f"{topic} {messagedata}"
    print(payload)
    sock.send_string(payload)               # Python 3 friendly
    time.sleep(1)
