# Automated Attendance Tracker Using Facial Recognition
The program is an automated attendance tracker that tracks the attendance of a person by recognising the face. The tracked attendance is stored in a CSV file format with the file name of the file titled according to the current date.

**NOTE**: To run this program successfully, create a folder and rename it as `Images_attendance` and save this folder in the same directory where the program `attendance.py` is stored. Inside the folder `Images_attendance`, add the image in .jpg/.jpeg/.png format and the rename the image as `1_[name].jpg/.jpeg/.png`, where `1` will be referred as the roll number and `[name]` will be the name of the person. Similarly, for the 2nd image, the image should be named as `2_[name].jpg/.jpeg/.png` and so on. For example, `1_AMEYA SHUKLA.JPG`

## Tech Stack
### Software 
- Language: Python (3.7.9)
- Libraries: OpenCV, numpy, pandas, cmake, dlib, [face-recognition](https://pypi.org/project/face-recognition/) (by Adam Geitgey)

### Hardware 
- Raspberry Pi Model 3B, Raspberry pi camera module Rev 1.3 

 

## Project Overview
This project addresses the structure, implementation and application of automated attendance tracker with the help of face recognition and identification which can be used in schools, colleges, offices and many other places where security and automation is required. Automated attendance system using face recognition is a system in which tracking of daily attendance is in an automatic manner and done by the program itself which is done by the recognition and identification of the face with the help of a camera module which is connected with the system. The camera module helps the system with the initial part of the program which is initialization of the camera on which the system can perform its operation. When the face comes in front of the camera, the program compares the face in the camera with the images in the database and recognizes it. These image data are basically known data for the system and is the data on which the system is trained. The system, if recognizes the face after the comparison with the database, displays the name of the person’s face or else displays “UNKNOWN” if the faces don’t match. Then it tracks the attendance of the person file of only the matched faces. This attendance is stored in an excel file format.

## Model Overview
The model relies on just a single camera to run. It accesses the camera and runs the program. For that, camera module is connected to the model. Then by just turning the switch on, the model will start performing its operation.

## Working
This system is based on face recognition which involves image processing and OpenCV library. The library is open source library supported by Python. When the software first runs it opens the camera connected to controller. When the camera is turned on it will scan the face that is which is in front of the camera. The image captured by camera will then be compared with the pre stored images in the system. When a face or multiple faces are in front of the camera, it starts to locate faces visible in the screen. This is done using the OpenCV and face-recognition libraries. OpenCV is used at the initial stage of the program at which the data processing is done. The data used here majorly are image data. Through the library, we can perform multiple operations such as accessing the camera, image reading, image cropping, conversion of image from BGR(Blue-Green-Red) to RGB(Red-Green-Blue) format for faster and efficient performance of the software, drawing rectangles around faces and adding text as well, and various other operations. The face-recognition library, on the other hand, is primarily used for locating faces and their identification. Using this library, we can find the faces in an image by finding their locations and also find their encodings. Once the software has found the face, it checks the face with the images stored in the database (known images) by comparing the encodings of the face seen in the screen with the encodings of the face in the images in the database. If the face matches with one of the faces in the database, it shows the name of the person’s face as a label in the webcam itself. If the face doesn’t match with the database images, then it labels the image as “UNKNOWN”. The software then stores the attendance of the person of the current date in an CSV file format. The software stores the attendance only if the faces match with the database which prevents false attendance. Also, the program creates a new file on every new date for attendance tracking which helps in maintaining attendance of the individual on each date. The data will be processed by the system using Raspberry Pi. Raspberry Pi is connected to the screen using Wi-fi. The camera module is connected to the dedicated slot available in raspberry pi. When the camera scans the image it will send the data to the raspberry pi and it will then process the scanned image. It will check the data(image) given by camera with pre stored data. If the data matches, it will store the attendance.

## Circuit
For the final circuit, the camera connected to Raspberry Pi model using camera module strip to the camera CSI port pin in Raspberry Pi as shown in Fig 6.4 below. Then, the model is connected to computer wirelessly through Wi-fi.  
When the connection is done, to switch on the model and automate the process, a 5V adapter is used to give power supply as the model runs on electricity. Finally, after switching on, the programs runs successfully.

 
 
![image](https://user-images.githubusercontent.com/58943665/125160171-29a72d80-e199-11eb-9e51-6791ff88d873.png)


![image](https://user-images.githubusercontent.com/58943665/125160227-6e32c900-e199-11eb-8840-8707197b7852.png)

![image](https://user-images.githubusercontent.com/58943665/125160243-7c80e500-e199-11eb-9fb2-9a6be4a1749e.png)

![image](https://user-images.githubusercontent.com/58943665/125160252-83a7f300-e199-11eb-9a2e-eb34c65e8f0c.png)


