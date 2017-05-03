#TugasPCD
#Khris Badawi [5301414041]
#Ubah tampilan warna Webcam menjadi hitam putih

import numpy as np
import cv2

capture = cv2.VideoCapture(0) #ntuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada laptop.

while (1): #untuk looping imshow, sehingga webcam akan menangkap objek video secara terus menerus sampai diberhentikan secara manual

	ret, img = capture.read() #menangkap gambar dengan format berwarna /BGR

	kodegray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #mengkonversi video dari warna ke grayscale
    
	cv2.imshow('Ori',img) #menampilkan citra dengan warna asli

	cv2.imshow('Gray',kodegray) #menampilkan citra grayscale
	if cv2.waitKey(1) & 0xFF == 27: #perintah untuk menghentikan program dengan menekan tombol esc pada keyboard
		break
	
cv2.destroyAllWindows()
capture.release()
