------------------------------------------------------------------------------------------
To run the object-color tracking code you need to do the following steps 
------------------------------------------------------------------------------------------


1- you need first to install the USB webcam driver using the following command from the raspberry pi

sudo apt-get install fswebcam

2- The color tracking range (minimum hue and maximum hue) can be changed via going to the following website and choosing the minimum values and maximum values for the selected color 

http://www.rapidtables.com/web/color/RGB_Color.htm

3- once the code locks on specific color, it will track it 

4- the code needs open cv libraries to be installed on the Raspberry pi, using the following link 

http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/

5- thats all