# Importing Image class from PIL module
from PIL import Image, ImageFilter
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

# Asks for the target directory and iterates
path = askdirectory(title='Select Image Folder') # shows dialog box and return the path
for x in os.listdir(path):
    if x.endswith(".jpg"):

        # Opens the target image and checks size
        imscale = Image.open(os.path.join(path, x)) # String interpretation issues caused path+x to fail (double '\\' escape char) 
        width, height = imscale.size
        #print("Original", imscale.size)
        
        # If image is greater than 1920px wide crop the image
        if (imscale.size[0]/imscale.size[1])>2:
            # Rescales the original image for the center print
            print(x)