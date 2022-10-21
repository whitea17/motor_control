import Jetson.GPIO as GPIO
import time

car_dir = 0  # f = 1, b = 2, fr = 3, fl = 4, br = 5, bl = 6

# GPIO pins
motor_pin_1 = 12
motor_pin_2 = 18
enable_pin = 13

#GPIO states
motor_pin_1_state = 0
motor_pin_2_state = 0
enable_pin_state = 0


def forward(speed):
  print("Going forward")
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_state

  motor_pin_1_state = 1
  motor_pin_2_state = 0
  enable_pin_state = 1


def backward(speed):
  print("Going backward at warp " + speed)
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_state

  motor_pin_1_state = 0
  motor_pin_2_state = 1
  enable_pin_state = 1


def forward_right(speed):
  print("Going forward right at warp " + speed)


def forward_left(speed):
  print("Going forward left at warp " + speed)


def backward_right(speed):
  print("Going backward warp " + speed)


def backward_left(speed):
  print("Going backward warp " + speed)


def main():
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_state

  # Setup
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(motor_pin_1, GPIO.OUT)
  GPIO.setup(motor_pin_2, GPIO.OUT)
  GPIO.setup(enable_pin, GPIO.OUT)

  # Loop
  while True:
    user_input = input(
      "Please enter a command, Ex: 1,2,2 means fwrd,fast,2 sec: ")
    user_input_split = user_input.split(",")

    dir = int(user_input_split[0])
    s = user_input_split[1]
    t = int(user_input_split[2])


    if (dir == 0):
      time.sleep(t)
      continue
    elif (dir == 1):
      forward(s)
    elif (dir == 2):
      backward(s)
    elif (dir == 3):
      forward_right(s)
    elif (dir == 4):
      forward_left(s)
    elif (dir == 5):
      print("doing 5")
      backward_right(s)
    elif (dir == 6):
      backward_left(s)

    print(motor_pin_1_state)
    GPIO.output(motor_pin_1, motor_pin_1_state)
    GPIO.output(motor_pin_2, motor_pin_2_state)
    GPIO.output(enable_pin, enable_pin_state)

    time.sleep(t)
    motor_pin_1_state = 0
    motor_pin2_state = 0
    enable_pin_state = 0
    GPIO.output(motor_pin_1, 0)
    GPIO.output(motor_pin_2, 0)
    GPIO.output(enable_pin, 0)

main()

