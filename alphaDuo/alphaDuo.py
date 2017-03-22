import RPi.GPIO as GPIO
import time
import argparse 
from __future__ import print_functino


class cameraSync(triggerPin=26):

    def __init__(self, self.triggerPin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.output(self.triggerPin, True)

    def run_test(self):
        for i in range(0, 10):
            time.sleep(0.50)
            GPIO.output(self.triggerPin, False)
            time.sleep(0.50)
            GPIO.output(self.triggerPin, True)

    def capture_stack(self, duration=24, delay=60):
        print('capture duration: '+str(duration))
        print('delay between captures: '+str(delay))
        duration_seconds = duration*60*60
        stop_t = time.time()+duration_seconds
        print('capture start time: ' str(time.asctime(time.time())))
        while time.time()<stop_t:
            time.sleep(delay-1)
            GPIO.output(self.triggerPin, False)
            time.sleep(1)
            GPIO.output(self.triggerPin, True)

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--test', help='run test: 10 images, 1 second between each', action='store_true')
    ap.add_argument('-c', '--capture', help='begin image stack capture', action='store_true')
    ap.add_argument('-d', '--delay', help='delay between images, in seconds; default = 60')
    ap.add_argument('-D', '--duration', help='duration of capture, in hours; default = 24')
    ap.add_argument('-p', '--pin', help='tigger pin designation; default = 26')
    args = vars(ap.parse_args())
    
    if args['pin']:
        cs = cameraSync(args['pin'])
    else:
        cs = cameraSync()

    if args['test']:
        cs.run_test()
    else:
        pass

    if args['delay']: 
        delay = args['delay']
    else:
        delay = 60

    if args['duration']:
        duration = args['duration']
    else:
        duration = 24

    if args['capture']:
        cs.capture_stack(duration, delay)
    else:
        pass

    print('capture stack finished @: ' time.asctime(time.time()))
