import sys
import zmq
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]

port2 = None
if len(sys.argv) > 2:
    port2 = sys.argv[2]

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)

print("Collecting updates from weather server...")
sock.connect(f"tcp://localhost:{port}")
if port2:
    sock.connect(f"tcp://localhost:{port2}")

# Subscribe to a specific topic. This is a prefix filter on the raw message.
topic_filter = "10001"
sock.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

# Optionally, wait a moment to ensure the subscription is registered
time.sleep(0.1)

total_value = 0
count = 5
for _ in range(count):
    msg = sock.recv_string()   # Python 3 friendly
    topic, messagedata = msg.split()
    print(topic, messagedata)
    total_value += int(messagedata)

print(f"Average messagedata value for topic '{topic_filter}' was {total_value / count:.1f}F")
