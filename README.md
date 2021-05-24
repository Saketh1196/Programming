# Programming

These are some of the mini projects done which are related to the field of Computer Vision. Image Classofication, Object detection, Text extraction from image, etc are some of the projects done and the used Libraries are OpenCV, matpotlib and Numpy. Along with this, I have created simple Graphical User Interface (GUI) projects using Python and MATLAB. 

These libraries are used in the following projects:

- OpenCV

 ```bash
  pip install opencv-python
 ```
- Matplotlib
 ```bash
  pip install matplotlib
 ```
- Numpy
 ```bash
   pip install numpy
  ```

## A. Image Classification

In this project, Images are loaded from the fashion MNIST dataset and is checked whether the images are correctly classified according to the given labels using the libraries 'keras' and 'Tensorflow'. They are further classified and trained under train and test images to obtain the desired results. 

- Tensorflow library
 ```
 pip install tensorflow
 ````

- Importing Keras library from Tensorflow
 ```
 from tensorflow import keras
 ````
### Steps Involved:

i. The names of the data in the dataset are classified into 9 different groups and are defined in a list.

ii. Image Preprocessing is done to convert the images into grey scale and displayed in order to ensure that the data that is being trained is correct or not.

iii. A neural network is defined to train the dataset containing images.
  1. The input layer for the network is of the shape 28*28.
  
  2. One hidden layer of size 128 neurons are used along with the activation function 'Relu'. If the computed value is negative then the result would be 0 and if the computed value is positive then the output value is 1.
  
  3. The output layer is defined with a size of 10 neurons.
  
iv. Now the model is compiled with adam optimizer and the accuracy and  losses are calculated.

v. Accuracy and losses are calculated by training the model with epoch (1 epoch is one set of Forward and Backward propagation).

vi. Predictions are now made on the image. When running the prediction it is observed that it returns the class name as a number for the output

vii. Two functions are defined to display the image and the corresponding bar graph indicating to the class to which the image belongs and how accurate the image is with the above trained and test accuracy.
  
Output:
![](Python/img_classification.jpg)

From the above Image, it can be viewed that the Images are classified correctly according to the given dataset. Blue color bar graph indicates that the image is recognised correctly and the green color bar graph indicates that the image has not been classified correctly according to the given conditions. The x-axis in the graph indicates the class names and the y-axis indicates the accuracy of the class names for the bar graph
 
### Note:
Sometimes there is a problem loading with the '.ipynb' extension file in the github repository. If you encouter this problem open the file with the given link below 'Image_Classification.ipynb':

[Image_Classification](https://nbviewer.jupyter.org/github/Saketh1196/Programming/blob/main/Python/Image_Classification.ipynb)

 
## B. Object Detection

In this task, a Car image with a license plate is given as input. 

### Steps involved: 

i. The Car image is displayed using "display function". Also, the image size and plotting is defined using this function.

ii. A Cascade Classifier is used to detect the object in the image. In this case, the license plate is the main object for detection.

iii. Next, a copy of the image is taken and is 'detectMultiScale' function is used. This function detects objects of different sizes in the given input image. The detected objects are returned as a list of rectangles.

iv. Using the cv2.rectangle function a rectangle box is drawn around the license plate of the image using the axis, height and width.

v. The required license plate is detected in the input image.

Output:
![](Python/car.jpg)
#### Note: 

Due to some issue the file is unable to load in the Github repository. It is resolved by opening the below link 'Object detection.ipynb':  

[Object detection.ipynb](https://nbviewer.jupyter.org/github/Saketh1196/Programming/blob/main/Python/Object%20detection.ipynb)

## C. Text Detection from image

The main goal is to detect text from a given image.

Used Modules for Extraction of the Image:
 
Once the text has been detected, bounding boxes are used to display the characters of the text individually as shown in the obtained result.

Output:
![](Python/tesseract.jpg)

### Note: 

Due to some issue the file is unable to load in the Github repository. It is resolved by opening the below link 'tesseract.ipynb: 

[tesseract.ipynb](https://nbviewer.jupyter.org/github/Saketh1196/Programming/blob/main/Python/tesseract.ipynb)


# GUI Projects

###  Simple GUI application of calculator using matlab
The code is presented in the MATLAB folder under the name "drunk_calculator.m"
This Calculator works as normal calculator when calculations are performed sequentially
Also this calculator have the capability to produce some wierd messages as displayed below. This happens when the buttons are pressed randomly.

![](MATLAB/drunk_calculator.png)   ![](MATLAB/drunk_calc.png)



#  PDFextractor 
 
It is an simple GUI app where the text can be extracted by uploading the desired pdf file.

The code is stored in the file 'PDFextractor.py'

These Libraries are used in the project

- tkinter - This library is used to create a graphic file. Different widgets like buttons, labels, Frame etc. are used in the project.

 ```bash
  pip install tk
 ```
- PyPDF2 - This library is used to perform several operations like splitting, merging, cropping etc on the uploaded pdf file.

 ```bash
  pip install PyPDF2
 ```
- PIL - Stands for Python imaging library, where it is supports opening, manipulating, saving different file formats.

 ```bash
  pip install Pillow
 ```
The ouptut of the program is attached as an image below along with the pdf file used in the program.

![](PDFextractor.png)


###  Login_System

This is a simple GUI app which makes allows the user to login into their account. The application consists of username password along with login and register options. The username and password will be created and stored in a text file for a new user. While on the other users, they can login with the details if their details are correct. If they are incorrect then the login will be prevented. 

It is built using Tkinter library where different widgets are used to control the application. Frmames, Labels, Entries, Canvas etc are some widgets which are used in this project. Also there are different functions present in the program to specify the operations being performed. 

- tkinter - This library is used to create a graphic file. Different widgets like buttons, labels, Frame etc. are used in the project.

 ```bash
  pip install tk
 ```

The code is stored in the file 'Login_System.py'

The ouptput of the code is shown as follows:

![](Screenshot%20(39).png)  ![](Screenshot%20(40).png)




