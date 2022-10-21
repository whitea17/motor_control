#include <Servo.h>

// Servo vars
Servo frontWheels;
int servo_pin = 5;
int servo_pos = 70;

// Input gpio pins to communicate desired dir. of wheels
int com_pin_1 = 6;
int com_pin_2 = 7;
int com_pin_1_state = LOW;
int com_pin_2_state = LOW;

void setup() {
  // Attach servo obj to servo pin
  frontWheels.attach(servo_pin);

  // Mark two com pins as inputs
  pinMode(com_pin_1, INPUT);
  pinMode(com_pin_2, INPUT);
}

void loop() {
  // Read com pin states
  com_pin_1_state = digitalRead(com_pin_1);
  com_pin_2_state = digitalRead(com_pin_2);

  // Based on read states, determine and set servo pos
  if(com_pin_1_state == LOW && com_pin_2_state == LOW){
    servo_pos = 90; // Center

  }else if(com_pin_1_state == LOW && com_pin_2_state == HIGH){
    servo_pos = 60; // Right
  }else if(com_pin_1_state == HIGH && com_pin_2_state == LOW){
    servo_pos = 115; // Left
  }

  frontWheels.write(servo_pos);
}
