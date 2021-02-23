from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import socket

options = {"Flag": 0, "copy": False, "track": False, "bidirectional_mode": True}

stream = VideoGear(source=0).start()

server = NetGear(
	address = str(socket.gethostbyname(socket.gethostname())),
	port = "5454",
	protocol = "tcp",
	pattern = 1,
	logging = True,
	**options
)

while True:
	try:
		frame = stream.read()
		if frame is None:
			break
		target_data = "SUP CUH"
		recv_data = server.send(frame, message=target_data)
		if not (recv_data is None):
			print(recv_data)
	except KeyboardInterrupt:
		break

stream.stop()
server.close()