import camera;

class Button:
  def press(self):
    new_photo = camera.Camera().take_photo();
    cmd = "fbi " + new_photo


