import time; 
import picamera;

class Camera:

  def get_rand_filename(self):
    return "/home/pi/photo_" + time.strftime("%d_%H:%M:%s") + ".jpg";

  def take_photo(self):
    print("Taking photo");
    filename = self.get_rand_filename();
    with picamera.PiCamera() as camera:
      camera.start_preview();
      time.sleep(5);
      camera.stop_preview();
      camera.capture(filename);
    print("Done");
    return filename;


