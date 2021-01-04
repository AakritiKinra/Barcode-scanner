from cv2 import cv2
from pyzbar import pyzbar
def read_barcode(frame):
    barcodes=pyzbar.decode(frame)
    for barcode in barcodes:
        x,y,width,height=barcode.rect
        data=barcode.data.decode('utf-8')
        type=barcode.type
        cv2.rectangle(frame, (x, y),(x+width, y+height), (0, 255, 0), 2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,data,(x,y),font,0.5,(0,0,0),1)
        print("Recognized {}: {}".format(type,data))
    return frame
def main():
    camera=cv2.VideoCapture(0)
    ret,frame=camera.read()
    while ret:
        ret,frame=camera.read()
        frame=read_barcode(frame)
        cv2.imshow('QR code reader', frame)
        if cv2.waitKey(1)==27:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()