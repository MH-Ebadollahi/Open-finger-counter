"""
Name of the program: hand and open fingers
                     detection

Porpuse of the program: input, from Python
                        image processing
                        program and
                        communication with
                        Siemens S7-1500
                        through OPC-UA
                        
Description: Siemens S7-1500 is activated
             for OPC-UA Server and 
             Python code is employed for client.


"""
import cv2, time
import mediapipe as mp
from opcua import Client
from opcua import ua


print("""\n welcome to the Hand Detection
 and
 Open-finger Counter Program
         \n\n developed by Mohammad Hossein Ebadollahi""")

print("\n")

server_address = input("""\n [*]Please enter the server address and port:\n\n
** Example Format: opc.tcp://255.255.255.255:0000 **
\n\n >> """)

node_address = input("""\n Please enter node ID from the server
\n\n Example format: ns=3;s="DB name"."Attribute name"
\n\n>> """)

client = Client(server_address)

client.connect()

print("""\n\n Client is Connected
\n\n Listening to the Server ...
\n\n Please wait... """)


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

new_frame_time = 0
prev_frame_time = 0


cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=2) as hands:
    
    while cap.isOpened():
        
        success,image = cap.read()

        image = cv2.flip(image,1)

        results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))


        hand = str(results.multi_handedness)

        if 'Right' in hand :
            whichhand = 'Hand : Right'
        elif 'Left' in hand :
            whichhand = 'Hand : Left'

        image.flags.writeable = True
        imageHeight, imageWidth, _ = image.shape
        

        gesture = 'Gesture : -'
        
        thumb = 0
        index = 0
        middle = 0
        ring = 0
        pincky = 0
        

        if results.multi_hand_landmarks :
            try :
                
                for hand_landmarks in results.multi_hand_landmarks :
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(16,31,235), thickness=4, circle_radius=3,), # Land Mark
                    mp_drawing.DrawingSpec(color=(52,235,155), thickness=2)) # Land Coonections                          
            


                    normalizedLandmark = hand_landmarks.landmark[3]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Thumb_Ip_x = pixelCoordinatesLandmark[0]
                    Thumb_Ip_y = pixelCoordinatesLandmark[1]
                
                    normalizedLandmark = hand_landmarks.landmark[4]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Thumb_Tip_x = pixelCoordinatesLandmark[0]
                    Thumb_Tip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[6] #point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Index_Pip_x = pixelCoordinatesLandmark[0]
                    Index_Pip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[8]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Index_Tip_x = pixelCoordinatesLandmark[0]
                    Index_Tip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[10] #point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Middle_Pip_x = pixelCoordinatesLandmark[0]
                    Middle_Pip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[12]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Middle_Tip_x = pixelCoordinatesLandmark[0]
                    Middle_Tip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[14] #point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Ring_Pip_x = pixelCoordinatesLandmark[0]
                    Ring_Pip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[16]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Ring_Tip_x = pixelCoordinatesLandmark[0]
                    Ring_Tip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[18]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Pinky_Pip_x = pixelCoordinatesLandmark[0]
                    Pinky_Pip_y = pixelCoordinatesLandmark[1]

                    normalizedLandmark = hand_landmarks.landmark[20]# point No.
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                    Pinky_Tip_x = pixelCoordinatesLandmark[0]
                    Pinky_Tip_y = pixelCoordinatesLandmark[1]

            
                    
                    if Thumb_Tip_x < Thumb_Ip_x and 'Right' in hand:
                        thumb = 1 
                    if Thumb_Tip_x > Thumb_Ip_x and 'Right' in hand:    
                        thumb = 0

                    if Thumb_Tip_x > Thumb_Ip_x and 'Left' in hand:
                        thumb = 1 
                    if Thumb_Tip_x < Thumb_Ip_x and 'Left' in hand:    
                        thumb = 0        

                    if Index_Tip_y < Index_Pip_y :
                        index = 1
                    if Index_Tip_y > Index_Pip_y :
                        index = 0

                    if Middle_Tip_y < Middle_Pip_y :
                        middle = 1
                    if Middle_Tip_y > Middle_Pip_y :
                        middle = 0

                    if Ring_Tip_y < Ring_Pip_y :
                        ring = 1
                    if Ring_Tip_y > Ring_Pip_y :
                        ring = 0

                    if Pinky_Tip_y < Pinky_Pip_y :
                        pincky = 1
                    if Pinky_Tip_y > Pinky_Pip_y :
                        rpincky = 0

                    hnd = thumb + index + middle + ring + pincky
                    print (whichhand ," //  Open fingers: ", hnd)    
    

                    if hnd == 0:
                        gesture = 'Gesture : Zero'
                    if hnd == 1:
                        gesture = 'Gesture : One'
                    if hnd == 2:
                        gesture = 'Gesture : Two'
                    if hnd == 3:
                        gesture = 'Gesture : Three'
                    if hnd == 4:
                        gesture = 'Gesture : Four'
                    if hnd == 5:
                        gesture = 'Gesture : Five'    
                    

                
                    cv2.rectangle(image,(5,4),(290,40),(0,170,240),-1)
                    cv2.putText(image,gesture,(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                    cv2.rectangle(image,(390,4),(640,40),(0,170,240),-1)
                    cv2.putText(image,whichhand,(400,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                    cv2.imshow('Hand Detection', image)

                    
                    finger_num = client.get_node('{}'.format(node_address))
                    set_finger = ua.DataValue(ua.Variant(hnd, ua.VariantType.Int16))
                    finger_num.set_value(set_finger)
                    
                    
            except TypeError :
                continue

        key = cv2.waitKey(1)
        if key == ord('q'):   
            cap.release()
            cv2.destroyAllWindows()
             
