import socket

from Robot import Robot

HOST = '127.0.0.1'
PORT = 54321

motor_1_pins = (22, 18, 16)
motor_2_pins = (15, 13, 11)
motor_3_pins = (40, 38, 36)


if __name__ == '__main__':
  Roboticop = Robot(motor_1_pins, motor_2_pins, motor_3_pins)

