from PIL import Image
import glob
from PIL import Image

def flat( *nums ):
    return tuple( int(round(n)) for n in nums )

class Size(object):
    def __init__(self, pair):
        self.width = float(pair[0])
        self.height = float(pair[1])

    @property
    def aspect_ratio(self):
        return self.width / self.height

    @property
    def size(self):
        return flat(self.width, self.height)

def cropped_thumbnail(img, size):
    original = Size(img.size)
    target = Size(size)

    if target.aspect_ratio > original.aspect_ratio:
        # image is too tall: take some off the top and bottom
        scale_factor = target.width / original.width
        crop_size = Size( (original.width, target.height / scale_factor) )
        top_cut_line = (original.height - crop_size.height) / 2
        img = img.crop( flat(0, top_cut_line, crop_size.width, top_cut_line + crop_size.height) )
    elif target.aspect_ratio < original.aspect_ratio:
        # image is too wide: take some off the sides
        scale_factor = target.height / original.height
        crop_size = Size( (target.width/scale_factor, original.height) )
        side_cut_line = (original.width - crop_size.width) / 2
        img = img.crop( flat(side_cut_line, 0,  side_cut_line + crop_size.width, crop_size.height) )
        
    return img.resize(target.size, Image.ANTIALIAS)

for filename in glob.glob('./train_imagenet_val/*.JPEG'):
    img = Image.open(filename)
    #img.thumbnail((256, 256),Image.ANTIALIAS)
    new_img=cropped_thumbnail(img, (256,256))
    filename=filename.split("/")[2]
    new_img.save("./train_imagenet_val1/"+filename, "JPEG", optimize=True)


for filename in glob.glob('./test_imagenet_val/*.JPEG'):
    img = Image.open(filename)
    print(img.size)
    new_img=cropped_thumbnail(img, (256,256))
    filename=filename.split("/")[2]
    print(new_img.size)
    new_img.save("./test_imagenet_val1/"+filename, "JPEG", optimize=True)
