import face_recognition
import cv2
import os
from datetime import *


# file/image loading
path = 'Images_attendance'

images = []
names_rolls = []

roll_nos = []
names = []

myList = os.listdir(path)
print('myList : ', myList)

for name_roll_jpg in myList:
    currImg = cv2.imread(f'{path}/{name_roll_jpg}')
    images.append(currImg)
    split_name_roll_jpg = (os.path.splitext(name_roll_jpg)[0])
    names_rolls.append(split_name_roll_jpg)
    #print(os.path.splitext(name))

for line in names_rolls:
    entry = line.split('_')
    #print(entry)
    roll_no = entry[0]
    #print(roll[0])
    roll_nos.append(roll_no)
    name = entry[1]
    names.append(name.upper())

print('roll_nos : ', roll_nos)
print('names : ', names)


# Encodings
def encodings(images):
    known_encodings = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        known_encodings.append(encode)
    return known_encodings

encodeListKnown = encodings(images)
print(len(encodeListKnown))
print('Encoding Complete')




# Marking the attendance in excel(.csv) file
def mark_attendance(name):

    dtString = date.today()                                                                                             # date today
    dtString_format = dtString.strftime('%d-%m-%Y')                                                                     # today's date in specified format

    nameList = []

    if os.path.exists(f'Attendance_{dtString_format}.csv') == False:
        with open(f'Attendance_{dtString_format}.csv', 'w') as f:                                                       # open a new file in write('w') format
            write = f.writelines('Roll Number, Name, Date, Time')                                                       # write the column names or the first row in the file
        with open(f'Attendance_{dtString_format}.csv', 'r+') as f:                                                      # then open the same file again, but in 'r+' format, because we need to read first and then write in the file at the same time
            myDataList = f.readlines()                                                                                  # read lines in the file which will be (['Name, Date, Time'])
            #print('myDataList : ', myDataList)


            for line in myDataList:                                                                                     # for each line in 'myDataList' which has read lines from the file
                entry = line.split(',')                                                                                 # split the lines after each comma like ('Name') and ('Date') seperated.
                nameOfPerson = entry[1]                                                                                 # after splitting, entry[0] will be 'Name'
                #print('nameOfPerson :', nameOfPerson)
                nameList.append(nameOfPerson)                                                                           # append it in the 'nameList' list
                #print('nameList :', nameList)

                if name not in nameList:                                                                                # if the name is not there in the 'nameList', then....
                    now = datetime.now()                                                                                # store the current time and date in the object 'now'
                    time_now = now.strftime('%H:%M:%S')                                                                 # store the time in the specified format ('%H:%M:%S')
                    date_now = now.strftime('%d-%m-%Y')
                    roll_no = roll_nos[first_match_index]
                    #nameList.append(name)

                    f.writelines(f'\n{roll_no},{name},{date_now},{time_now}')                                           # then write the name of the person and the time in the file

                    #print('nameList :', nameList)                                                                      # prints the 'nameList' list which contains the category 'Name' and name of the identified face('Ameya Shukla', 'Elon Musk',....)



    elif os.path.exists(f'Attendance_{dtString_format}.csv') == True:
        with open(f'Attendance_{dtString_format}.csv', 'r+') as f:                                                      # then open the same file again, but in 'r+' format, because we need to read first and then write in the file at the same time
            myDataList2 = f.readlines()                                                                                 # read lines in the file which will be (['Name, Date, Time'])
            #print('myDataList2 :', myDataList2)
            #print('nameList :', nameList)

            for line in myDataList2:                                                                                    # for each line in 'myDataList' which has read lines from the file
                entry = line.split(',')                                                                                 # split the lines after each comma like ('Name') and ('Date') seperated.
                #print('entry : ', entry)
                nameOfPerson = entry[1]                                                                                 # after splitting, entry[0] will be 'Name'
                #print('entry[0]', entry[0])
                nameList.append(nameOfPerson)                                                                           # append it in the 'nameList' list
                #print('nameList : ', nameList)

            if name not in nameList:                                                                                    # if the name is not there in the 'nameList', then....
                now = datetime.now()                                                                                    # store the current time and date in the object 'now'
                time_now = now.strftime('%H:%M:%S')                                                                     # store the time in the specified format ('%H:%M:%S')
                date_now = now.strftime('%d-%m-%Y')
                roll_no = roll_nos[first_match_index]


                f.writelines(f'\n{roll_no},{name},{date_now},{time_now}')                                                     # then write the name of the person and the time in the file
    # #         print(nameList)                                                                                        # prints the 'nameList' list which contains the category 'Name' and name of the identified face('Ameya Shukla', 'Elon Musk',....)




# webcam
web_cap = cv2.VideoCapture(0)

# Initializing some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = web_cap.read()

    # Resizing frame to 1/4th size for faster face recognition processing
    resized_frame = cv2.resize(frame, (0,0), None, fx=0.25, fy=0.25)

    # Convert the image from BGR to RGB
    rgb_resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_resized_frame)
        face_encodings = face_recognition.face_encodings(rgb_resized_frame, face_locations)


        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(encodeListKnown, face_encoding)

            # Declaring (name = 'Unknown') by default
            name = 'UNKNOWN'

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                 first_match_index = matches.index(True)                                                                # gives the index position of the identified face in the webcam from the file path('Images Attendance') only if the face matches. Else keep 'Unknown' by default
                 name = names[first_match_index]                                                                        # 'name' object takes the index position and 'names' list and then if the face matches, identifies the name from the 'names' list at that index position('first_match_index')
                 roll_no = roll_nos[first_match_index]
                 #print(roll_no)
                 #print(name)
                 mark_attendance(name)

            face_names.append(name)                                                                                     # Now, append each identified 'name' to 'face_names' list
    #print(face_names)
    process_this_frame = not process_this_frame                                                                         # Now, we exit the for loop and turn this condition False



    # Display the results
    for (t, r, b, l), name in zip(face_locations, face_names):

        #print(name)
        # Scale back up face locations since the frame we detected in was scaled to 1/4th size
        t *= 4
        r *= 4
        b *= 4
        l *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (l, t), (r, b), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (l, b - 35), (r, b), (0, 0, 255), cv2.FILLED)

        cv2.putText(frame, name, (l + 6, b - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)


    cv2.imshow('Attendance Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
web_cap.release()
cv2.destroyAllWindows()

