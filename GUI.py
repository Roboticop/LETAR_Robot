import PySimpleGUI as sg
import cv2

class GUI():
    def __init__(self):
        layout = [
            [sg.Image(filename = "", key = "display_image")],
        ]
        self.window = sg.Window("Project LETAR", layout, location = (800, 400))