import os.path
import time

class Location(object):
    #24 * 60 * 60
    def __init__(self, status_file, duration, interval, preferred_hour, name, start_function, stop_function):
        self.status_file = status_file
        self.duration = duration
        self.interval = interval
        self.name = name
        self.preferred_hour = preferred_hour
        self.start_function = start_function
        self.stop_function = stop_function

    def last_watering(self):
        stamp = 0

        if os.path.exists(self.status_file):
            fo = open(self.status_file, 'r')
            temp = fo.read()

            try:
                stamp = int(temp)
            except:
                stamp = 0
            fo.close()

        return stamp

    def mark_watering(self, stamp):

        fo = open(self.status_file, 'w')
        fo.write(str(stamp))
        fo.close()

    def is_watering_needed(self):
        last_stamp = self.last_watering()
        now_stamp = int(time.time())

        # We wait for the time to be updated
        if last_stamp > now_stamp:
            return False

        diff = now_stamp - last_stamp

        # Once a day
        if diff > self.interval:
            return True

        local_time = time.localtime(now_stamp)

        if local_time.tm_hour == self.preferred_hour \
                and diff > min(2 * 60 * 60, self.interval):
            return True

        return False

    def perform_watering(self):
        self.start_function()
        time.sleep(self.duration)
        self.stop_function()

    def water(self):
        if self.is_watering_needed():
            self.perform_watering()
            self.mark_watering(int(time.time()))