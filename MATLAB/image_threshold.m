% In this task a threshold value is considered for the given image and if
% the pixel value is greater than the specified value it is converted to
% brighter pixel otherwise converted to darker pixel

orig_img= imread("giraffes.jpg");
img1 = rgb2gray(orig_img);
img1 = double(img1);
[rows columns] = size(img1);
for i = 1:rows
    for j = 1:columns
        if img1>127
            img1(i,j)=255; % 255 indicates brighter pixel
        else
            img1(i,j)=0;   % 0 indicates darker pixel
        end
    end
end
%plotting the figures and comparing with original image
subplot(1,2,1);
imshow(orig_img)
subplot(1,2,2);
imshow(img1)
