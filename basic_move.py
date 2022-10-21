import Jetson.GPIO as GPIO
import time

# GPIO pins
motor_pin_1 = 12
motor_pin_2 = 32
enable_pin = 33

#GPIO states
motor_pin_1_state = 0
motor_pin_2_state = 0
enable_pin_pwm_val = 0
enable_pin_pwm = None

def forward(speed):
  print("Going forward")
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_pwm_val

  motor_pin_1_state = 1
  motor_pin_2_state = 0
  enable_pin_pwm_val = speed

def backward(speed):
  print("Going backward at warp " + str(speed))
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_pwm_val

  motor_pin_1_state = 0
  motor_pin_2_state = 1
  enable_pin_pwm_val = speed


def forward_right(speed):
  print("Going forward right at warp " + str(speed))


def forward_left(speed):
  print("Going forward left at warp " + str(speed))


def backward_right(speed):
  print("Going backward warp " + str(speed))


def backward_left(speed):
  print("Going backward warp " + str(speed))

# Set GPIO pin's actual states based off of specified states via variables
def setGPIO():
  global GPIO
  global enable_pin_pwm

  GPIO.output(motor_pin_1, motor_pin_1_state)
  GPIO.output(motor_pin_2, motor_pin_2_state)
  enable_pin_pwm.ChangeDutyCycle(enable_pin_pwm_val)

# Initial GPIO setup
def setupGPIO():
  global GPIO
  global enable_pin_pwm_val
  global enable_pin_pwm

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(motor_pin_1, GPIO.OUT)
  GPIO.setup(motor_pin_2, GPIO.OUT)
  GPIO.setup(enable_pin, GPIO.OUT, initial=GPIO.HIGH)

  enable_pin_pwm = GPIO.PWM(enable_pin, 50)
  enable_pin_pwm.start(0)

# Reset variables that represent state of pins to default values
def resetStates():
  global motor_pin_1_state
  global motor_pin_2_state
  global enable_pin_pwm_val

  motor_pin_1_state = 0
  motor_pin2_state = 0
  enable_pin_pwm_val = 0

def main():
  # Setup
  setupGPIO()

  # Loop
  while True:
    user_input = input(
      "Please enter a command, Ex: 1,2,2 means fwrd,fast,2 sec: ")
    user_input_split = user_input.split(",")

    dir = int(user_input_split[0])
    s = int(user_input_split[1])
    t = int(user_input_split[2])

    # Interpert command and adjust vars
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

    print(enable_pin_pwm_val)
    # Execute current loop's command based on var states
    setGPIO()

    # Wait specified time
    time.sleep(t)

    # Reset vars and GPIO states
    resetStates()
    setGPIO()


main()

