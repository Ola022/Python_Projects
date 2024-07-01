import cv2

""" [ pip install opencv-contrib-python ]

    Capture image from mobile camera by connecting the camera through  `ivCamera mobile and desktop App`
    1-- Download the `ivCam` App on System and SmartPhone(Browsing phone )
    2-- Install the app on each device and grant all access from the prompt (Allow the app through FIREWALL, 
        if not exit craete)
    3-- Connect the phone and laptop to the same network or connect them through cable wire
    4-- Lunch the app in both device
    5-- Get the laptop IP-Address and input it to ur mobile system or Vice-Versa
    6-- Press connect 
    
    Note:   IPhone XR is used for testing, and app wont be available for connection 
            if you not charging the phone
"""

cap = cv2.VideoCapture(1)
#address = "http://169.254.203.224:8080/"
#address = "http://172.20.10.3:8080"
address = "http://172.20.10.3"

#ccap.open(address)

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
    if cv2.waitKey(20) == ord("a"):
        cv2.imwrite("image.png", frame)


cap.release()
cv2.destroyAllWindows()