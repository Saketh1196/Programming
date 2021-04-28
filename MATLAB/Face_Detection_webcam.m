%The objective of the task is to detect Face using the webcam of your
%computer.

clc
clear all
web=webcam();           % function to open webcam 
img=snapshot(web);      % captures the image to be detected
dete= vision.CascadeObjectDetector(); % function to detect object 
imshow(img);

while true
    img=snapshot(web);
    im2=rgb2gray(img);
    bbox=step(dete,im2);
    pic=insertObjectAnnotation(img,'rectangle',bbox,'Face');
    imshow(pic);
  
end
