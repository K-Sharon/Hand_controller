import cv2
import mediapipe as mp
import pyautogui
import time
cam=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
draw_utils=mp.solutions.drawing_utils
screen_w,screen_h=pyautogui.size()
Thumb_x,Thumb_y,Mid_x,Mid_y=0,0,0,0
last_time=0
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_weight,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_weight)
                y=int(landmark.y*frame_height)

                if id==8:
                    cv2.circle(frame,(x,y),10,(0,255,0),2)
                    x1=int(landmark.x*screen_w)
                    y1=int(landmark.y*screen_h)
                    pyautogui.moveTo(x1,y1)
                if id==4:
                    cv2.circle(frame,(x,y),10,(255,0,0),2)
                    Thumb_x=int(landmark.x*screen_w)
                    Thumb_y=int(landmark.y*screen_h)
                if id==12:
                    cv2.circle(frame,(x,y),10,(255,0,0),2)
                    Mid_x=int(landmark.x*screen_w)
                    Mid_y=int(landmark.y*screen_h)

                if(abs(Thumb_x-Mid_x)<50 and abs(Thumb_y-Mid_y) <50 ):
                    cur_time=time.time()
                    if cur_time-last_time >0.5:
                        pyautogui.click()
                        last_time=cur_time
                        print(abs(Thumb_x-Mid_x), " ", abs(Thumb_y-Mid_y))
                        print("click")



    cv2.imshow('Hand Controller',frame)
    cv2.waitKey(1)
