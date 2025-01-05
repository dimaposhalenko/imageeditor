from PIL import Image
from PIL import ImageFilter


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.origanal = None
        self.changed = list()


    def open(self):
        try: 
            self.origanal = Image.open(self.filename)
        except:
            print('Файл не знайдено!')
        self.origanal.show()
    def black_white(self):
        bw_photo = self.origanal.convert('L')
        self.changed.append(bw_photo)
        bw_photo.show()


    def do_left(self):
        rotated = self.origanal.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.show()


    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.origanal.crop(box)
        self.changed.append(cropped)
        cropped.show()

MyImage = ImageEditor('pig.jpg')
MyImage.open()

MyImage.black_white()

MyImage.do_left()

MyImage.do_cropped()