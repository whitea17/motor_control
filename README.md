# Motor Control Solution for Intel Jetson Nano
### What is this?
A Python program that emulates RC car like motor control.
There is a basic program and a class-ified version that handles commnuication to a ln298n motor controller and a servo motor.

### Why the Arduino Program?
The Intel Jetson Nano GPIO operates at 3.3v while I only had access to a 5v servo. The 5v servo was not recognizing 3.3v PWM signals from the Intel Jetson Nano. An Arduino Nano acts as a middle man, translating ln298n-like GPIO commnunication from the Jetson Nano to the 5v servo. Instead of forwards, or backwards, the two GPIO pins signaled one of positions (Left, Right, Center).

**See this repo for how the library is used:** https://github.com/whitea17/ISTUD_AI_CAR
