import pylablib as pll
import cv2 as cv
import numpy as np
import time

from pylablib.devices import Thorlabs

with Thorlabs.ThorlabsTLCamera('22554') as cam:
    cam.set_exposure(3E-2)  # set 30ms exposure
    # cam.set_frame_period(5E-2)
    cam.set_frame_info_period(5E-2)
    cam.start_acquisition()
    
    frame_count = 1
    while True:
        print(frame_count)
        rtn = cam.wait_for_frame(timeout=1)  # wait for the next available frame
        
        
        frame=cam.read_oldest_image()  # get the oldest image which hasn't been read yet
        frame_converter = np.zeros((frame.shape[0], frame.shape[1], 1), dtype=np.uint8)
        frame_converter[:, :, 0] = frame
        cv.imshow('Video', frame_converter)
        if cv.waitKey(1) & 0xFF==ord('d'):
            break

        frame_count += 1

    cam.stop_acquisition()
cv.destroyAllWindows()
    