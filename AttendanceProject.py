import csv
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
images =[]
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    currentImg = cv2.imread(f'{path}/{cl}')               #f  is for filename   To read the file
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return  encodeList

def markAttendance(name):
    with open(filename,'r+') as f:
        myDataList = f.readlines()
        # print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%d/%b/%Y, %a, %H:%M:%S')
            f.writelines(f'\n{name},{dtString}')




encodeListKnown = findEncodings(images)
# print(len(encodeListKnown))
print('Encoding Complete')
videoCapture = cv2.VideoCapture(0)

# Define the fields that will be used as column headers in the CSV file
fields = ['Name','Date','Day', 'Time']

filename = datetime.now().strftime('Attendance-%Y-%m-%d.csv')
with open(filename,"w+") as f:
    # Create a CSV writer object that will write to the file 'f'
    write = csv.writer(f)
    # Write all of the rows of data to the CSV file
    write.writerow(fields)


# now = datetime.now()
# current_date = now.strftime("%Y-%m-%d")
# f = open(current_date+'.csv','w+',newline = '')
# lnwriter = csv.writer(f)

while True:
    success, img = videoCapture.read()
    imageSmall = cv2.resize(img,(0,0),None,0.25,0.25)
    imageSmall = cv2.cvtColor(imageSmall, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(imageSmall)
    encodesCurrentFrame = face_recognition.face_encodings(imageSmall,facesCurrentFrame)

    for encodeFace,faceLoc in zip(encodesCurrentFrame,facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam',img)
    # cv2.waitKey(1)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
videoCapture.release()
cv2.destroyAllWindows()
from subprocess import call

def open_py_file():
    call(["python","LoadingCSVFiles.py"])

open_py_file()   


