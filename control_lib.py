import time
import RPi.GPIO as GPIO


POWER_SLEEP_TIME_SECONDS = 2


class ControlRelays(object):

    def __init__(self):
        self.relay_pins = [3, 5, 7, 13]

        self.power_pin = self.relay_pins[0]
        self.outer_pin = self.relay_pins[1]
        self.living_room_pin = self.relay_pins[2]
        self.office_room_pin = self.relay_pins[3]

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        for pin in self.relay_pins:
            GPIO.setup(pin, GPIO.OUT)

        self.stop_all()

    def turn_on_pin(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def turn_off_pin(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def stop_all(self):
        for pin in self.relay_pins:
            self.turn_off_pin(pin)

    def turn_on_power(self):
        self.turn_on_pin(self.power_pin)

        # Wait for it to spin up
        time.sleep(POWER_SLEEP_TIME_SECONDS)

    def turn_off_power(self):
        self.turn_off_pin(self.power_pin)

    def turn_on_outer(self):
        self.turn_on_pin(self.outer_pin)

    def turn_off_outer(self):
        self.turn_off_pin(self.outer_pin)

    def turn_on_living_room(self):
        self.turn_on_pin(self.living_room_pin)

    def turn_off_living_room(self):
        self.turn_off_pin(self.living_room_pin)

    def turn_on_office_room(self):
        self.turn_on_pin(self.office_room_pin)

    def turn_off_office_room(self):
        self.turn_off_pin(self.office_room_pin)