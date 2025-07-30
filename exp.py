import glob
from PIL import Image, ImageOps
import time

foreground1 = Image.open("18.png")
foreground2 = ImageOps.flip(foreground1)
foreground1.paste(foreground2, (0, 0), foreground2)
foreground3 = ImageOps.mirror(foreground1)
foreground1.paste(foreground3, (0, 0), foreground3)

imc = 0

for imd in glob.glob("testdata/flowcam_polina_pontoon_0907_r2/rawfile*.tif"):
    background = Image.open(imd)
    background.paste(foreground1, (0, 0), foreground1)

    background.save("testout/imc" + str(imc)  +".jpg")
    imc += 1
