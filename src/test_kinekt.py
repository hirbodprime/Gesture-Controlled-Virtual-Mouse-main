import cv2
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime

def test_kinect():
    kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

    while True:
        if kinect.has_new_color_frame():
            frame = kinect.get_last_color_frame()
            image = frame.reshape((1080, 1920, 4)).astype('uint8')
            cv2.imshow('Kinect Video Stream', cv2.cvtColor(image, cv2.COLOR_RGBA2RGB))
        
        key = cv2.waitKey(1)
        if key == 27:  # ESC key
            cv2.destroyAllWindows()
            kinect.close()
            break

test_kinect()
