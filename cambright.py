#TugasPCD
#Khris Badawi [5301414041]
#Ubah tampilan warna Webcam menjadi lebih cerah

import numpy as np
import cv2

capture = cv2.VideoCapture(0) #ntuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada laptop.
alpha = 1.5 #mengubah nilai brightness, semakin tinggi nilai semakin menuju warna putih
beta = 25 #mengubah nilai brightness, semakin tinggi nilai semakin menuju warna putih
while (1): #untuk looping imshow, sehingga webcam akan menangkap objek video secara terus menerus sampai diberhentikan secara manual

	ret, img = capture.read() #menangkap gambar dengan format berwarna /BGR

	kodecerah = cv2.addWeighted(img,alpha, np.zeros(img.shape, img.dtype), 0, beta) #mengubah brightness citra berwarna / BGR
	
	kodegray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #mengkonversi frame dari warna ke grayscale
    
	cv2.imshow('Ori',img) #menampilkan citra dengan warna asli

	cv2.imshow('Brighter',kodecerah) #menampilkan citra berwarna dengan brightness yang telah diubah
	if cv2.waitKey(1) & 0xFF == 27: #perintah untuk menghentikan program dengan menekan tombol esc pada keyboard
	    break
	
cv2.destroyAllWindows()
capture.release()
