# Importing Image class from PIL module
from PIL import Image, ImageFilter
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

path = askdirectory(title='Select Folder') # shows dialog box and return the path
for x in os.listdir(path):
    if x.endswith(".jpg"):
        # Prints only JPEG files present in selected directory
        print(path+x)
        imscale = Image.open(os.path.join(path, x))

        # Rescales the original image for the center print
        imscale = Image.open(os.path.join(path, x))
        width, height = imscale.size
        print("Original", imscale.size)
        scale = 1920, 1080
        imscale.thumbnail(scale, Image.Resampling.LANCZOS)
        width, height = imscale.size
        print("Rescale", imscale.size)
        RescaleWidth = imscale.size[0]
        # imscale.show()

        # Crops the original image and blurs
        imcrop = Image.open(os.path.join(path, x))
        width, height = imcrop.size
        cropscale = 1920, (1920/imcrop.size[0])*imcrop.size[1]
        imcrop.thumbnail(cropscale, Image.Resampling.LANCZOS)
        center = imcrop.size[1]/2
        top = center+540
        bottom = center-540
        cropbox = (0, bottom, 1920, top)
        crop = imcrop.crop(cropbox)
        print("Crop", imcrop.size)
        gaussImage = crop.filter(ImageFilter.GaussianBlur(20))

        # Pastes the scaled image over the blured image
        shift = int((1920-RescaleWidth)/2), 0
        print("Shift", shift)
        gaussImage.paste(imscale, shift)
        gaussImage.show()
        imscale.close()
        imcrop.close()
        gaussImage.close
        
# Sources Image Manipulation
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
# https://www.geeksforgeeks.org/python-pil-image-crop-method/ 
# https://www.geeksforgeeks.org/python-pil-image-resize-method/
# https://www.geeksforgeeks.org/python-pil-image-thumbnail-method/
# https://www.tutorialspoint.com/python_pillow/python_pillow_blur_an_image.htm
# https://note.nkmk.me/en/python-pillow-paste/#:~:text=Call%20the%20paste()%20method,left)%20of%20the%20base%20image.
# https://pillow.readthedocs.io/en/latest/reference/Image.html (Image.paste)
# https://www.geeksforgeeks.org/how-to-convert-float-to-int-in-python/

# Select images and directories.
# https://stackoverflow.com/questions/50860640/ask-a-user-to-select-folder-to-read-the-files-in-python
# 
#
#