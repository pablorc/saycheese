import time; import picamera;

class Camera:

  def get_rand_filename(self):
    return "/home/pi/photo_" + time.strftime("%d_%H:%M:%s") + ".jpg";

  def take_photo(self):
    print("Taking photo");
    with picamera.PiCamera() as camera:
      time.sleep(5);
      camera.capture(self.get_rand_filename());
      camera.stop_preview();
    print("Done");

