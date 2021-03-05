from movement import XY_Motor_Movement, Z_Motor_Movement

class Robot(XY_Motor_Movement, Z_Motor_Movement):

  def __init__(self, motor_1_pins, motor_2_pins, motor_3_pins):
    XY_Motor_Movement.__init__(self, motor_1_pins, motor_2_pins)
    Z_Motor_Movement.__init__(self, motor_3_pins)
    self.classification_dictionary = {
      "FORWARD": self.Move_Forward,
      "BACKWARD": self.Move_Backward,
      "RIGHT": self.Move_Right,
      "LEFT": self.Move_Left,
      "STOP": self.Stop_Moving,
    }

  def movement_classifier(self, recieved_string):
    self.classification_dictionary[recieved_string]()
  