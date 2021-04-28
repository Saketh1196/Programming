% The main objective of this task is to detect face features for a given
% facial image and labelling the parts in the picture.

clc
clear all

img = imread('scarlett.jpg');
%pic = rgb2gray(img);
%rimshow(pic);

% To detect Right Eye in the image
detect_REye = vision.CascadeObjectDetector('RightEye');
detect_REye.MergeThreshold=200;
boundingbox = step(detect_REye,img);
Right_Eye = insertObjectAnnotation(img,'rectangle',boundingbox,'RightEye');

% To detect Left Eye in the image
detect_LEye = vision.CascadeObjectDetector('LeftEye');
detect_LEye.MergeThreshold=250;
boundingbox1 = step(detect_LEye,img);
Left_Eye = insertObjectAnnotation(img,'rectangle',boundingbox1,'LeftEye');

% To detect Nose in the image
detect_Nose = vision.CascadeObjectDetector('Nose');
detect_Nose.MergeThreshold=10;
boundingbox = step(detect_Nose,img);
Nose = insertObjectAnnotation(img,'rectangle',boundingbox,'Nose');

% To detect Mouth in the image
detect_Mouth = vision.CascadeObjectDetector('Mouth');
detect_Mouth.MergeThreshold=300;
boundingbox = step(detect_Mouth,img);
Mouth= insertObjectAnnotation(img,'rectangle',boundingbox,'Mouth');

a=cat(2,Right_Eye,Left_Eye,Nose,Mouth);
imshow(a)

