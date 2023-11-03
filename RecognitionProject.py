import cv2
import numpy as np
import face_recognition
import os
import tkinter

from time import sleep
from datetime import datetime
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

path = 'ImagesRecord'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print("------------------------------------\n")
print("------------------------------------\n\nAuthorised users are:\n")
print(classNames)
print("------------------------------------\n")
print("------------------------------------\n")


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAccess(name):
    with open('AccessRecord.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

encodeListKnown = findEncodings(images)
print('Encoding of the authorised user images completed!')
print("------------------------------------\n")


def startCap():
    
    global cap
    cap = cv2.VideoCapture(0)
    countAllowed = 0
    countNotAllowed = 0
    while True:
        # sleep(1)
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print("Difference in comparison: ")
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                countNotAllowed=0
                countAllowed += 1
                print("Frame number: ", countAllowed)

                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                if countAllowed>=20:
                    countAllowed=0
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showwarning("Warning", "Hello :) Access Verified ! \n You are allowed to access the system!")
                    sleep(2)
                    return
            else:
                name = "Unknown"
                countAllowed=0
                countNotAllowed += 1
                print("Frame number: ", countNotAllowed)

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                if countNotAllowed>=25:
                    countNotAllowed=0
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showwarning("Warning", "Warning: Access Denied ! \n You are not allowed to access the system")
                    sleep(2)
                    return

            markAccess(name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)

def stopCap():
    cap.release()  
    cv2.destroyAllWindows()

win = Tk()

# Set the size of the tkinter window
win.geometry("1500x900")
win.wm_title("FaceLock App")
# Add an optional Label widget
Label(win, text= "Welcome !", font= ('Aerial 17 bold italic')).pack(pady= 30)
Label(win, text= "Verify the User Login:", font= ('Aerial 12 bold')).pack(pady= 50)
 

# Create a Button to display the message
ttk.Button(win, text= "Start", command=startCap).pack(pady= 20)
ttk.Button(win, text= "Stop", command=stopCap).pack(pady= 20)
win.mainloop()
