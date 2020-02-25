import sys, os
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk
import time
import glob
import cv2

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')


def showPIL(pilImage):
    #imgWidth, imgHeight = pilImage.size
 # resize photo to full screen 
    #ratio = min(w/imgWidth, h/imgHeight)
    #imgWidth = int(imgWidth*ratio)
    #imgHeight = int(imgHeight*ratio)
    #pilImage = pilImage.resize((imgWidth,imgHeight), Image.NEAREST)   
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    #root.update_idletasks()
    root.update()
#    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

names = glob.glob('cache/*')
print(names)
while True:
    for file in names:
        if file.split('.')[-1] == 'mp4':
            print('video')
            start = time.time()
            video = cv2.VideoCapture(file)
            while True:
                ret,frame = video.read()
                if ret:
                    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    frame = Image.fromarray(frame)
                    showPIL(frame)
                else:
                    print('time taken:',(time.time()-start))
                    break


        elif file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'png':
            print(file)
            media_file=Image.open(file)
            showPIL(media_file)
            sleep_duration = file.split('.')[0].split('_')[-1]
            print(sleep_duration)
            time.sleep(int(sleep_duration))
        else:
            print('format not supported')