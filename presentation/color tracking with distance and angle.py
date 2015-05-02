#Import OpenCV
import cv2
#Import Numpy
import numpy as np
import time

camera_feed = cv2.VideoCapture(0)


while(1):

    _,frame = camera_feed.read()
    #Convert the current frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   

    #Define the threshold for finding a blue object with hsv
    lower_blue = np.array([70,100,30])
    upper_blue = np.array([130,255,150])
   

    #Create a binary image, where anything blue appears white and everything else is black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Get rid of background noise using erosion and fill in the holes using dilation and erode the final image on last time
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    mask = cv2.erode(mask,element, iterations=2)
    mask = cv2.dilate(mask,element,iterations=2)
    mask = cv2.erode(mask,element)
    
    #Create Contours for all blue objects
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maximumArea = 0
    bestContour = None
    for contour in contours:
        currentArea = cv2.contourArea(contour)
        if currentArea > maximumArea:
            bestContour = contour
            maximumArea = currentArea
     #Create a bounding box around the biggest blue object
    if bestContour is not None:
        x,y,w,h = cv2.boundingRect(bestContour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)

       # print (w)
       # print (h)
        # print (y)

        distance = (1804.1 * (w **-1.145))
        time.sleep(1)
        print("Distance=")
        print (distance)
        print('     ')

        mid=x+(w/2)
        angle = (mid/5) + 15

        print('angle is ')
        print(angle)

       # print(mid)
        
        
        #if w > 100:
          # print ('distance is about 1 foot')
            
        #if w > 50 and w < 100:
          # print ('distance is about 2 feet')
                
        #if w > 25 and w < 50:
         #  print ('distance is about 3 feet')
                    
        #if w > 17 and w < 25:
           #print ('distance is about 4 feet')
                        
        #if w >12 and w < 17:
           #print ('distance is about 5 feet')
                            
        #if w < 12:
           #print ('distance is about 6 feet')

                                
            
        
      #  elif w > 50 and w < 100:
      #  print ('distance is approximately 2 feet')
      #  elif w > 25 and w < 50:
      #  print ('distance is approximately 3 feet')
       # elif w > 17 and w < 25:
       # print ('distance is approximately 4 feet')
       # elif w >12 and w <17:
       # print ('distance is about 5 feet')
       # else:
       # print ('distance is about 6 feet')
        
        

    #Show the original camera feed with a bounding box overlayed 
    cv2.imshow('frame',frame)
    #Show the contours in a seperate window
    cv2.imshow('mask',mask)
    #Use this command to prevent freezes in the feed
    k = cv2.waitKey(5) & 0xFF
    #If escape is pressed close all windows
    if k == 27:
        break


cv2.destroyAllWindows() 
