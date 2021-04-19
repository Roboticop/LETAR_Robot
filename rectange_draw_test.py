from vidgear.gears import VideoGear
import cv2

from GUI import GUI

stream = VideoGear(source = 0).start()

if __name__ == '__main__':
    graphics = GUI()
    while True:
        event, values = graphics.window.read(timeout = 1)
        frame = stream.read()
        start_point = (640 // 4, 480 // 3)
        end_point = (640 * 3 // 4, 480 * 2 // 3)
        color = (255, 0, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        graphics.window["display_image"].update(data = imgbytes)