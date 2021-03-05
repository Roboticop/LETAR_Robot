import l293d

class XY_Motor_Movement():
  '''Motors will set up the robots motors and functions will be called to move the robot'''
  def __init__(self, motor_1_pins, motor_2_pins):
    self.left_motor = l293d.DC(motor_1_pins[0], motor_1_pins[1], motor_1_pins[2])
    self.right_motor = l293d.DC(motor_2_pins[0], motor_2_pins[1], motor_2_pins[2])
  
  def Move_Forward(self):
    self.left_motor.anticlockwise()
    self.right_motor.clockwise()

  def Move_Backward(self):
    self.left_motor.clockwise()
    self.right_motor.anticlockwise()

  def Move_Right(self):
    self.left_motor.clockwise()
    self.right_motor.clockwise()

  def Move_Left(self):
    self.left_motor.anticlockwise()
    self.right_motor.anticlockwise()

  def Stop_Moving(self):
    self.left_motor.stop()
    self.right_motor.stop()

  def XY_MOTOR_TEST(self):
    try:
      self.left_motor.clockwise(duration=0.5)
      self.right_motor.clockwise(duration=0.5)
      self.left_motor.anticlockwise(duration=0.5)
      self.right_motor.anticlockwise(duration=0.5)
    except:
      print("Something is wrong with the XY Motors.")


class Z_Motor_Movement():
  '''Motor that adjusts the height of the robot'''
  def __init__(self, motor_3_pins):
    self.z_motor = l293d.DC(motor_3_pins[0], motor_3_pins[1], motor_3_pins[2])

  def Move_Up(self):
    self.z_motor.clockwise()

  def Move_Down(self):
    self.z_motor.anticlockwise()

  def Z_Motor_Stop(self):
    self.z_motor.stop()

  def Z_MOTOR_TEST(self):
    try:
      self.z_motor.clockwise(duration=0.5)
      self.z_motor.anticlockwise(duration=0.5)
    except:
      print("An error has occured with the Z motor.")