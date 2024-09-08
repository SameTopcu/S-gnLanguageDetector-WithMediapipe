import numpy as np
import mediapipe as mp
from Function import *


#Mediapipe'in Hands modülünü tanımladık.
holy_hands = mp.solutions.hands

#Kendi webcamımızden görüntü almak için videocapture nesnesini oluşturduk.
cap = cv.VideoCapture(0)


#Mediapipenin Hands modülünü kullanarak el tespiti yapıyoruz.
with holy_hands.Hands(
    max_num_hands=1 
                      ) as hands:
   
  #İzleme noktalarının koordinatlarını saklamak için bir liste oluşturduk.
   index_cord=[] 

   #Kamera her açık olduğunda bu eylemi gerçekleştir :
   while cap.isOpened():
     #kameradan resimleri oku.
     success, image = cap.read()
     if not success:
       #Kamera boş kare gönderirse uyarı ver.
       print("Boş kamera çerçevesi göz ardı ediliyor.")
       continue

     #Görüntüyü RGB formatına dönüştürüyoruz.
     image.flags.writeable = False
     image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

     #Görüntüdeki elleri tespit ediyoruz.
     results = hands.process(image)

     #Görüntüyü yazılabilir moda getirip BGR formatına dönüştürüyoruz.
     image.flags.writeable = True
     image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    
      #Görüntünün yüksekliğini ve genişliğini alıyoruz.
     imgH,imgW=image.shape[:2]
     ## Tanımlanan işaret dili karakterini saklamak için boş bir string oluşturuyoruz.
     string=''

     #Eğer el tespiti olursa elin koordinatlarını bulmak için sorgu yazdık.
     if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks:
         hand_cordinate=[]
         for index , landmark in enumerate(hand_landmarks.landmark):
            x_cordinate , y_cordinate = int(landmark.x*imgW) , int(landmark.y*imgH)
            hand_cordinate.append([index,x_cordinate,y_cordinate])
            #Elin koordinatlarını numpy array'e dönüştürüyoruz.
         hand_cordinate=np.array(hand_cordinate)

          # Koordinatları kullanarak işaret dili karakterini tanımlıyoruz.
         string=persons_input(hand_cordinate)


         # Tanımlanan karakteri görüntüye ekliyoruz.
         image=get_fram(image,hand_cordinate,string)

     if string==" D" :
          index_cord.append([15,hand_cordinate[8][1],hand_cordinate[8][2]])
     if string==" I" or string==" J":
          index_cord.append([15,hand_cordinate[20][1],hand_cordinate[20][2]])

          # İzleme noktalarını çember şeklinde ekle.
     for val in index_cord:
          image=cv.circle(image,(val[1],val[2]),val[0],(255,255,255),1)
          val[0]=val[0]-1
          if val[0]<=0:
              index_cord.remove(val)
      ## Görüntüyü ekranda gösteriyoruz.        
     cv.imshow('Sign Language detection', cv.flip(image,1))


      #Döngüden çıkmak için x tuşuna bas.Kamerayı kapat.
     if cv.waitKey(5) & 0xFF == ord('x'):
       break
     
 #Kameranın kapanması.    
cap.release()

