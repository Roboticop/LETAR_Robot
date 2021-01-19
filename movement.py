import l293d

class XY_Motor_Movement():
  '''Motors will set up the robots motors and functions will be called to move the robot'''
  def __init__(self, motor_1_pins, motor_2_pins):
    self.left_motor = l293d.DC(motor_1_pins)
    self.right_motor = l293d.DC(motor_2_pins)
  
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

  def Stop_moving(self):
    self.left_motor.stop()
    self.right_motor.stop()

class Z_Motor_Movement():
  '''Motor that adjusts the height of the robot'''
  def __init__(self, motor_3_pins):
    self.z_motor = l293d.DC(motor_3_pins)

  def Move_Up(self):
    self.z_motor.clockwise()

  def Move_Down(self):
    self.z_motor.anticlockwise()