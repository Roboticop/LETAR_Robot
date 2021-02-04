from vidgear.gears import VideoGear
from vidgear.gears import NetGear

from Robot import Robot

ADDRESS = '127.0.0.1'
PORT = "5454"

options = {"flag": 0, "copy": False, "track": False, "bidirectional_mode": True, "secure_mode": 2}

stream = VideoGear(source = 0).start()

server = NetGear(
    address = ADDRESS,
    port = PORT,
    protocol = "tcp",
    pattern = 1,
    logging = True,
    **options
)

motor_1_pins = (22, 18, 16)
motor_2_pins = (15, 13, 11)
motor_3_pins = (37, 36, 33)


if __name__ == '__main__':
    Roboticop = Robot(motor_1_pins, motor_2_pins, motor_3_pins)

    while True:
        try:
            frame = stream.read()
            if frame is None:
                break
            target_data = "SUP"
            recv_data = server.send(frame, message = target_data)
            if not (recv_data is None):
                print(recv_data)
        except KeyboardInterrupt:
            break

    stream.stop()
    server.close()


