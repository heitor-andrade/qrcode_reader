from pyzbar.pyzbar import decode
import cv2
import numpy as np


# input: cv2 image
# output: data, pts_arr
#       data is the qrcode information
#       pts_arr is list that with the coordinates of each qrcode 
#                each coordinates is a array (4, 2) with the x and y of the 4 quarters of the qrcode       
def qrcode_read(input_frame):
    try:
        code = decode(input_frame)
    except:
        return [], []
    
    if len(code) == 0:
        return [], []
    pts_arr = []
    data = []
    for obj in code:
        # get text and points
        text = obj.data.decode('utf-8')
        pts = np.array(obj.polygon, np.int32)
        
        if obj.type == "QRCODE":
            # pts = pts.reshape((4, 2))
            pts_arr.append(pts)
            data.append(text)

            # draw polygon around qrcode
            pts = pts.reshape((4, 1, 2))
            cv2.polylines(input_frame, [pts], True, (255, 100, 5), 2)
            # cv2.putText(input_frame, text, (50, 50), cv2.FONT_HERSHEY_PLAIN,1.5,(255,100,5),2) # draw the text of qrcode in the screen
    return data, pts_arr

# input: cv2 image
# output: data
#       data is the barcode information
def barcode_read(input_frame):
    try:
        code = decode(input_frame)
    except:
        return []
    if len(code) == 0:
        return []
    data = []
    for obj in code:
        # get text and points
        text = obj.data.decode('utf-8')
        pts = np.array(obj.polygon, np.int32)
        
        if obj.type != "QRCODE":
            data.append(text)
            cv2.putText(input_frame, text, (50, 50), cv2.FONT_HERSHEY_PLAIN,1.5,(255,100,5),2) # draw the text of qrcode in the screen
        else:
            print("len pts = ", len(pts))
    return data
