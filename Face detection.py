import zipfile
import PIL
from PIL import Image,ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
from matplotlib.pyplot import imshow

fh = open("image.zip", "rb")
files = zipfile.ZipFile(fh)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
for i, img in eumerate(files.namelist()):
    files.extract(img)
    image = cv.imread(img)
    images = []
    flag = 0
    #display(image)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.01)
    first_image = list(faces[0])
    #print(first_image)
    print("Results found in file "+img)
    contact_sheet = PIL.Image.new("RGB" , (first_image[2]*50, first_image[3]*50))
    for x,y,w,h in faces:
        face = Image.open(img).convert("RGB")
        crop_face = face.crop(box = (x,y,x+w,y+h))
        crop_face = crop_face.resize((first_image[2],first_image[3]))
        #display(crop_face)
        images.append(crop_face)
        flag  = 1
    if(flag != 1):
        print("But there were no faces in that file")
        continue
    xaxis = 0; yaxis = 0
    if(flag == 0): print("")
    for f in images:
        contact_sheet.paste(f, (xaxis, yaxis))
        if xaxis+first_image[2] == contact_sheet.width:
            xaxis=0
            yaxis=yaxis+first_image[3]
        else:
            xaxis=xaxis+first_image[2]
    #contact_sheet = contact_sheet.resize((int(contact_sheet.width),int(contact_sheet.height) ))
    contact_sheet.save("finimage_{}.jpeg".format(str(i))
    #if(True): break
