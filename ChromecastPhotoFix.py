# Importing Image class from PIL module
from PIL import Image, ImageFilter
 
# Rescales the original image for the center print
imscale = Image.open(r"C:\Users\Eric\Pictures\ChromecastFix\Original\49214503798_03b510311d_k.jpg")
width, height = imscale.size
print("Original", imscale.size)
scale = 1920, 1080
imscale.thumbnail(scale, Image.Resampling.LANCZOS)
width, height = imscale.size
print("Rescale", imscale.size)
RescaleWidth = imscale.size[0]
# imscale.show()

# Crops the original image and blurs
imcrop = Image.open(r"C:\Users\Eric\Pictures\ChromecastFix\Original\49214503798_03b510311d_k.jpg")
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

# Sources Image Manipulation
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
# https://www.geeksforgeeks.org/python-pil-image-crop-method/ 
# https://www.geeksforgeeks.org/python-pil-image-resize-method/
# https://www.geeksforgeeks.org/python-pil-image-thumbnail-method/
# https://www.tutorialspoint.com/python_pillow/python_pillow_blur_an_image.htm
# https://note.nkmk.me/en/python-pillow-paste/#:~:text=Call%20the%20paste()%20method,left)%20of%20the%20base%20image.
# https://pillow.readthedocs.io/en/latest/reference/Image.html (Image.paste)
# https://www.geeksforgeeks.org/how-to-convert-float-to-int-in-python/