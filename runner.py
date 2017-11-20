from control_lib import ControlRelays
from locations import Location
import logging
from subprocess import call

def main():
    rc = ControlRelays()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='/home/pi/sprinkler.log',
                        filemode='a')

    try:
        outer = Location('/home/pi/outer_stat',
                         300,
                         24 * 60 * 60,
                         7, 'outer',
                         rc.turn_on_living_room,
                         rc.turn_off_living_room)

        outer2 = Location('/home/pi/outer2_stat',
                          730,
                          24 * 60 * 60,
                          7,
                          'outer2',
                          rc.turn_on_outer,
                          rc.turn_off_outer)


        outer_needed = outer.is_watering_needed()
        outer2_needed = outer2.is_watering_needed()

        if outer_needed or outer2_needed:
            logging.info('Turning on power')
            rc.turn_on_power()

            if outer_needed:
                logging.info('Outer watering started')
                outer.water()
                logging.info('Outer watering ended')

            if outer2_needed:
                logging.info('Outer 2 watering started')
                outer2.water()
                logging.info('Outer 2 watering ended')

            logging.info('Turning off power')
            rc.turn_off_power()

        else:
            logging.info('No need to run')

    except Exception as e:
        logging.error(str(e))
        rc.stop_all()
    finally:
        call("sync")


if __name__ == '__main__':
    main()
