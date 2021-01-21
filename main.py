import socket

from Robot import Robot

HOST = '127.0.0.1'
PORT = 65432

motor_1_pins = (22, 18, 16)
motor_2_pins = (15, 13, 11)
motor_3_pins = (37, 36, 33)


if __name__ == '__main__':
  Roboticop = Robot(motor_1_pins, motor_2_pins, motor_3_pins)

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
      print('Connected by', addr)
      while True:
        data = conn.recv(1024)
        print(data)
        decoded_data = data.decode()
        if "quit" in decoded_data:
          break
        elif "test" in decoded_data:
          Roboticop.XY_MOTOR_TEST()
          Roboticop.Z_MOTOR_TEST()
        elif "Movement" in decoded_data:
          if "forward" in decoded_data:
            Roboticop.Move_Forward()
          elif "right" in decoded_data:
            Roboticop.Move_Right()
          elif "left" in decoded_data:
            Roboticop.Move_Left()
          elif "back" in decoded_data:
            Roboticop.Move_Backward()
          elif "up" in decoded_data:
            Roboticop.Move_Up()
          elif "down" in decoded_data:
            Roboticop.Move_Down()
          else:
            Roboticop.Stop_moving()
            Roboticop.Z_Motor_Stop()
        conn.sendall(data)

