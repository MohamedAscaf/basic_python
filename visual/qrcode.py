import qrcode
img = qrcode.make("jayaram")
img.save("img1.jpg")




""" import cv2
qr_img = cv2.imread("img1.jpg")
qr_det = cv2.QRCodeDetector()
val,pts,st_code = qr_det.detectAndDecode(qr_img)
print("information",val) """
