import Jetson.GPIO as GPIO
import time

class MotorControl:
	def __init__(self, motor_pin_1, motor_pin_2, enable_pin, servo_pin_1, servo_pin_2):
		# GPIO pins
		self.motor_pin_1 = motor_pin_1
		self.motor_pin_2 = motor_pin_2
		self.enable_pin  = enable_pin
		self.servo_pin_1 = servo_pin_1
		self.servo_pin_2 = servo_pin_2

		#GPIO states
		self.motor_pin_1_state = 0
		self.motor_pin_2_state = 0
		self.enable_pin_pwm_val = 0
		self.enable_pin_pwm = None
		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 0

		# Setup gpio for use
		self.setupGPIO()


	def forward(self, speed=50):
		print("Going forward")

		self.motor_pin_1_state = 1
		self.motor_pin_2_state = 0

		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 0

		self.enable_pin_pwm_val = speed


	def backward(self, speed=50):
		print("Going backward at warp " + str(speed))

		self.motor_pin_1_state = 0
		self.motor_pin_2_state = 1

		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 0

		self.enable_pin_pwm_val = speed


	def forward_right(self, speed=50):
		print("Going forward right at warp " + str(speed))

		self.motor_pin_1_state = 1
		self.motor_pin_2_state = 0

		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 1

		self.enable_pin_pwm_val = speed

	def forward_left(self, speed=50):
		print("Going forward left at warp " + str(speed))

		self.motor_pin_1_state = 1
		self.motor_pin_2_state = 0

		self.servo_pin_1_state = 1
		self.servo_pin_2_state = 0

		self.enable_pin_pwm_val = speed


	def backward_right(self, speed=50):
		print("Going backward warp " + str(speed))

		self.motor_pin_1_state = 0
		self.motor_pin_2_state = 1

		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 1

		self.enable_pin_pwm_val = speed


	def backward_left(self, speed=50):
		print("Going backward warp " + str(speed))

		self.motor_pin_1_state = 0
		self.motor_pin_2_state = 1

		self.servo_pin_1_state = 1
		self.servo_pin_2_state = 0

		self.enable_pin_pwm_val = speed


	# Set GPIO pin's actual states based off of specified states via variables
	def setGPIO(self):
		global GPIO
		GPIO.output(self.motor_pin_1, self.motor_pin_1_state)
		GPIO.output(self.motor_pin_2, self.motor_pin_2_state)

		GPIO.output(self.servo_pin_1, self.servo_pin_1_state)
		GPIO.output(self.servo_pin_2, self.servo_pin_2_state)

		self.enable_pin_pwm.ChangeDutyCycle(self.enable_pin_pwm_val)


	# Initial GPIO setup
	def setupGPIO(self):
		global GPIO

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.motor_pin_1, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.motor_pin_2, GPIO.OUT, initial=GPIO.LOW)

		GPIO.setup(self.servo_pin_1, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.servo_pin_2, GPIO.OUT, initial=GPIO.LOW)

		GPIO.setup(self.enable_pin, GPIO.OUT, initial=GPIO.HIGH)

		self.enable_pin_pwm = GPIO.PWM(self.enable_pin, 50)
		self.enable_pin_pwm.start(0)


	# Reset variables that represent state of pins to default values
	def resetStates(self):
		self.motor_pin_1_state = 0
		motor_pin2_state = 0

		self.servo_pin_1_state = 0
		self.servo_pin_2_state = 0

		self.enable_pin_pwm_val = 0


