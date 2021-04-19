from vidgear.gears import VideoGear, PiGear
from vidgear.gears import NetGear
import pyaudio
import json
import serial
from gtts import gTTS
from playsound import playsound
import time

from GUI import GUI

ADDRESS = '127.0.0.1'
PORT = "5454"

options = {"flag": 0, "copy": False, "track": False, "bidirectional_mode": True, "secure_mode": 2}

#VidGear Implimentation
netgear_stream = VideoGear(source = 0).start()

#PiGear Implimentation
#netgear_stream = PiGear(camera_num = 0).start()

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

#Audio speaking stuff
language = "en"

def send_audio_video():
    event, values = graphics.window.read(timeout = 1)
    frame = netgear_stream.read()
    target_data = audio_stream.read(CHUNK)
    target_data = target_data.decode('ISO-8859-1')
    recv_data = server.send(frame, message = target_data)
    start_point = (640 // 4, 480 // 3)
    end_point = (640 * 3 // 4, 180 * 2 // 3)
    color = (255, 0, 0)
    thickness = 2
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    graphics.window["display_image"].update(data = imgbytes)

def speek_audio(message):
    speak_message = "Please align the barcode of your driver's license with the square on the screen"
    speech = gTTS(text = speak_message, lang = language, slow = False)
    speech.save("speech.mp3")
    playsound("speech.mp3")

if __name__ == '__main__':
    ser = serial.Serial(serial_port, serial_baud_rate, timeout = 1)
    ser.flush()

    graphics = GUI()

    while True:
        try:
            frame = netgear_stream.read()
            if frame is None:
                break
            target_data = audio_stream.read(CHUNK)
            target_data = target_data.decode('ISO-8859-1')
            recv_data = server.send(frame, message = target_data)
            speak_message = ""
            if recv_data != None:
                if recv_data == "MF":
                    #Move the robot forwards
                    ser.write(b'F')
                elif rev_data == "SM":
                    #Stop the robot
                    ser.write(b'O')
                elif recv_data == "DLR":
                    #Detect Driver's License
                    start_time = time.time()
                    speek_audio("Please align the barcode of your driver's license with the rectangle on the screen")
                    while time.time() < start_time + 2:
                        send_audio_video()
                    speek_audio("3")
                    while time.time() < start_time + 3:
                        send_audio_video()
                    speek_audio("2")
                    while time.time() < start_time + 4:
                        send_audio_video()
                    speek_audio("1")
                    while time.time() < start_time + 5:
                        send_audio_video()
                    speek_audio("Say Cheese")
                    while time.time() < start_time + 5.5:
                        frame = netgear_stream.read()
                        recv_data = server.send(frame, message = "DETECT")
                elif recv_data == "RR":
                    #Detect Registration
                    start_time = time.time()
                    speek_audio("Please align the barcode of your car registration with the rectangle on the screen")
                    while time.time() < start_time + 2:
                        send_audio_video()
                    speek_audio("3")
                    while time.time() < start_time + 3:
                        send_audio_video()
                    speek_audio("2")
                    while time.time() < start_time + 4:
                        send_audio_video()
                    speek_audio("1")
                    while time.time() < start_time + 5:
                        send_audio_video()
                    speek_audio("Say Cheese")
                    while time.time() < start_time + 5.5:
                        frame = netgear_stream.read()
                        recv_data = server.send(frame, message = "DETECT")
                elif recv_data == "0":
                    speak_message = "Do you know why I pulled you over?"
                elif recv_data == "1":
                    speak_message = "Where are you coming from?"
                elif recv_data == "2":
                    speak_message = "Have you been drinking tonight?"
                elif recv_data == "3":
                    speak_message = "How many drinks have you had?"
                elif recv_data == "4":
                    speak_message = "How long did you wait in between each drink?"
                elif recv_data == "5":
                    #get out the breathalyzer
                    speak_message = "Blow into this please"
                elif "speak" in recv_data:
                    speak_message = recv_data[5::]
                elif recv_data = "DONE":
                    #Move the robot back to the police officer and tell the person to have a nice day
                    ser.write(b'B')
                    speak_message = "Thank you very much.  Have a nice day!"
            if speak_message != "":
                speech = gTTS(text = speak_message, lang = language, slow = False)
                speech.save("speech.mp3")
                playsound("speech.mp3")
                speak_message = ""
            if not (recv_data is None):
                if recv_data is not None:
									if "M" in recv_data:
										recv_data = recv_data[-1]
										ser.write(str.encode(recv_data))
        except KeyboardInterrupt:
            break

    audio_stream.stop()
    server.close()


