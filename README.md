# Facelock-App
## An AI based Facial Recognition Solution For Vulnerabilities in Smart Home Systems
#
### Tools Used:
#### Built with:
- Python 3.9
#### Modules/Libraries used:
- opencv-python 4.5.3.56
- dlib 19.18.0
- numpy 1.19.Orc1
- cmake 3.21.3
- face-recognition 1.3.0
#### Software used:
- Visual Studio Code
#### Explanation:
- OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human.
- Dlib is a facial detector with pre-trained models, the dlib is used to estimate the location of 68 coordinates (x, y) that map the facial points on a person's face.
- NumPy is a Python library used for working with arrays.
- Cmake allows the path to an imported library to be used without having to know what type of library it is.
# 
### Flowchart:
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/422a27ac-92f9-4b1f-a3ee-001995866b96)
#
### Algorithm:

1.	The first step is enrollment, we will store the images of authorized people in a separate folder as a database that we can access in future to record and verify the access.
2.	Then, we start the camera for video capturing.
3.	The video will have some frames per second rate - fps rate. So, we extract each frame from the incoming video.
4.	Then, for each extracted frame we do face detection.
5.	Next step will be face recognition by comparison with the stored images. It will compare the incoming face with the stored ones, if it matches, allow the user and mark the access. Otherwise, go for next frames.
6.	It will continue the loop for some frames specified by us, if the face doesn't match it won't allow access to that person.
7.	If the user in the camera already has an entry in the file then nothing will happen. The name of the user along with the current time stamp will be stored. 
8.	If the person is unknown, so we change the name to ‘unknown’ and don’t allow the access as well as send the mail to the concerned authorities.

#
### Execution: 
#### 
- Run the '.py' file:
####
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/3bdb480f-826f-4101-93d2-054646c8b3e6)
####
### Output Screenshots:
####
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/abcb80b3-5c7f-4861-a2ab-8c651c3edd6e)
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/929a9452-667f-40cd-93d0-16228d68e87e)
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/1e91e6c0-87aa-433a-99bf-d7d9214917d6)
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/921141f6-7165-4ca8-83e7-54c6539167fd)
####
#### It shows a green frame with the name only for allowed person's face, and a red frame around the unknown (unauthorised) users with a Warning - "Access Denied !".
####
### Records:
####
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/c3ad08cc-14fd-45a9-9378-41763aef785d)
####
![image](https://github.com/NIRANJAN-K-DESHMUKH/Facelock-App/assets/82277471/0a306629-c1d0-4016-a8b7-aae2430eb552)
####
