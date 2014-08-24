import button;
import time;
import RPi.GPIO as GPIO;

class ConsoleView: 

  def run(self):
    self.run_infinite_loop()

  def run_infinite_loop(self):
    while(True):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.wait_for_edge(17, GPIO.FALLING)
      button.Button().press()

  def run_evented(self):
    self.prepare_button();
    raw_input("Press [ENTER] to exit");

  def prepare_button(self):
    print("Preparing GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.FALLING)
    #GPIO.add_event_callback(17, self.photo_requested)
    GPIO.add_event_callback(17, self.blink)
    print("GPIO prepared")

  def photo_requested(self, another):
    print("photo requested")
    print(time.time())
    print(another)
    button.Button().press();

  def blink(self, another):
    print("blink")
    print(time.time())

    
