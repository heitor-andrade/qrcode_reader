from code_reader import qrcode_read, barcode_read
import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    text_qr, pts_qr = qrcode_read(frame)
    text_bar = barcode_read(frame)
    if len(pts_qr) != 0:
        print("QRCODE: ", text_qr, pts_qr)
    if len(text_bar) != 0:
        print("BARCODE: ", text_bar)

    cv2.imshow("DD", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()