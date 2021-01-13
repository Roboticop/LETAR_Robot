import l293d

class Motors():
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
