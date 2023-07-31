# Importing Image class from PIL module
from PIL import Image, ImageFilter
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

# Asks for the target directory and iterates
path = askdirectory(title='Select Image Folder') # shows dialog box and return the path
savepath = askdirectory(title='Select Resize Save Directory')
for x in os.listdir(path):
    if x.endswith(".jpg"):

        # Opens the target image and checks size
        imscale = Image.open(os.path.join(path, x)) # String interpretation issues caused path+x to fail (double '\\' escape char) 
        width, height = imscale.size
        #print("Original", imscale.size)
        
        # If image is greater than 1920px wide crop the image
        if imscale.size[0]>1920:
            # Rescales the original image for the center print
            scale = 1920, 1080
            imscale.thumbnail(scale, Image.Resampling.LANCZOS)
            width, height = imscale.size
            #print("Rescale", imscale.size)
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
            #print("Crop", imcrop.size)
            gaussImage = crop.filter(ImageFilter.GaussianBlur(20))

            # Pastes the scaled image over the blured image
            shift = int((1920-RescaleWidth)/2), 0
            #print("Shift", shift)
            gaussImage.paste(imscale, shift)
            #gaussImage.show()
            
            # Saves Image
            savename = x.replace(".jpg", "_CCResize.jpg")
            gaussImage.save(os.path.join(savepath, savename), format='JPEG', subsampling=0, quality=95) #PIL default JPEG compression values lead to poor image quality
            print("Resize")

            # Closes open image objects
            gaussImage.close()
            imcrop.close()
            imscale.close()

        # If the image is less than or equal to 1920px wide copy to the new save directory
        elif 1:
            imscale.save(os.path.join(savepath, x), format='JPEG', subsampling=0, quality=95)
            print("Copy")
            imscale.close()

        
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
# https://stackoverflow.com/questions/24678604/how-can-i-use-a-variable-instead-of-a-path-to-open-an-image-file-using-pil-in-py

# Save images
# https://www.geeksforgeeks.org/python-pil-image-save-method/

# Poor Image Quality
# https://stackoverflow.com/questions/19303621/why-is-the-quality-of-jpeg-images-produced-by-pil-so-poor