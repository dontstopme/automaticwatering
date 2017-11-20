#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

out_pins = [3, 5, 7, 11]

for pin in out_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)
