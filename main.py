from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import pyaudio

from Robot import Robot

ADDRESS = '127.0.0.1'
PORT = "5454"

options = {"flag": 0, "copy": False, "track": False, "bidirectional_mode": True, "secure_mode": 2}

netgear_stream = VideoGear(source = 0).start()

server = NetGear(
    address = ADDRESS,
    port = PORT,
    protocol = "tcp",
    pattern = 1,
    logging = True,
    **options
)

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
audio_stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK
)

motor_1_pins = (22, 18, 16)
motor_2_pins = (15, 13, 11)
motor_3_pins = (37, 36, 33)


if __name__ == '__main__':
    Roboticop = Robot(motor_1_pins, motor_2_pins, motor_3_pins)

    while True:
        try:
            frame = netgear_stream.read()
            if frame is None:
                break
            target_data = audio_stream.read(CHUNK)
						target_data = JSON.parse(target_data)
            recv_data = server.send(frame, message = target_data)

            if not (recv_data is None):
                if recv_data is not None:
                    Roboticop.movement_classifier(recv_data)
                    print(recv_data)
        except KeyboardInterrupt:
            break

    stream.stop()
    server.close()


