from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import pyaudio
import json
import serial

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

serial_port = '/dev/ttyACMO'    #Change this to the Raspberry Pi specific port
serial_baud_rate = 10000    #Eventually I'll pick a better port, but for now
# Use ser.write(b'F' b'B' b'L' b'R' or b'O') to move the motor

if __name__ == '__main__':
    ser = serial.Serial(serial_port, serial_baud_rate, timeout = 1)
    ser.flush()

    while True:
        try:
            frame = netgear_stream.read()
            if frame is None:
                break
            target_data = audio_stream.read(CHUNK)
            target_data = target_data.decode('ISO-8859-1')
            recv_data = server.send(frame, message = target_data)
            if not (recv_data is None):
                if recv_data is not None:
                    Roboticop.movement_classifier(recv_data)
                    print(recv_data)
        except KeyboardInterrupt:
            break

    stream.stop()
    server.close()


