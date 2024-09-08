# SıgnLanguageDetector-WithMediapipe
 The application was developed using Mediapipe and opencv.
# Hand Gesture Recognition System

Bu proje, bilgisayar kamerası kullanarak işaret dili karakterlerini tanımlayan ve bunları ekrana görüntüleyen bir el hareketi tanıma sistemidir. Sistem, Python ve OpenCV kullanılarak geliştirilmiştir ve elin pozisyonlarına ve parmakların durumuna göre işaret dili karakterlerini belirler.

## Proje Yapısı

Proje, iki Python dosyasından oluşmaktadır:

- **Function.py**: İşlevlerin ve el hareketi tanıma algoritmalarının tanımlandığı dosya.
- **Main.py**: Ana dosya, el hareketlerini tanımlamak ve kullanıcıya görsel olarak göstermek için kullanılır.

### 1. Function.py

`Function.py` dosyasında, elin pozisyonlarına ve parmakların durumuna göre işaret dili karakterlerini belirlemek için çeşitli fonksiyonlar tanımlanmıştır.

#### Öne Çıkan Fonksiyonlar:

- **`persons_input(hand_cordinates)`**: Elin koordinatlarını alır ve parmakların yukarıda veya aşağıda olup olmadığını belirleyerek işaret dili karakterini tanımlar.
  
- **`get_fram(image, hand_cordinate, string)`**: Belirli koordinatlara göre görüntüye kırmızı bir dikdörtgen çizer ve işaret dili karakterini ekler.

Aşağıda bu fonksiyonlardan birinin örnek kullanımını görebilirsiniz:

```python
def persons_input(hand_cordinates):
    def distance(x1, y1, x2, y2):
        # Öklid mesafe formülü ile mesafeyi ayarlar
        distance = int((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2))
        return distance
    
    # İşaret dili karakterlerini belirleme mantığı...
    
    return persons_input
```
### Main.py

`Main.py` dosyası, proje için ana çalıştırma dosyasıdır ve işaret dili karakterlerinin tanınması ve ekranda görüntülenmesi işlemlerini gerçekleştirir.

Bu dosyada:

- **Mediapipe** kullanılarak gerçek zamanlı el tespiti yapılır.
- Tespit edilen elin koordinatları kullanılarak işaret dili karakterleri belirlenir.
- Tanımlanan karakterler ve el pozisyonu ekrana çizilir.
- ### Örnek Kullanım

```python
import numpy as np
import mediapipe as mp
from Function import *

# Kamerayı başlatma ve el tespiti yapma
cap = cv.VideoCapture(0)

with mp.solutions.hands.Hands(max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Boş kamera çerçevesi göz ardı ediliyor.")
            continue
        
        # İşlem ve tespit kodları...
        
        cv.imshow('Sign Language Detection', cv.flip(image, 1))
        
        # Döngüden çıkmak için 'x' tuşuna basın
        if cv.waitKey(5) & 0xFF == ord('x'):
            break

cap.release()
```
### Gereksinimler

Projeyi çalıştırmak için gereken kütüphaneler:

- OpenCV
- Mediapipe
- Numpy

### Kurulum

Gerekli kütüphaneleri kurmak için terminale aşağıdaki komutları girin:

```bash
pip install opencv-python mediapipe numpy
```
### Kullanım
Sistemi başlatmak için `Main.py` dosyasını çalıştırın. Kamera açılacak ve el hareketlerinizi tanıyarak işaret dili karakterlerini ekrana yansıtacaktır. Programdan çıkmak için 'x' tuşuna basın.

### Uygulamadan Örnekler
- ![image](https://github.com/user-attachments/assets/11cc8e74-b642-4c41-ba63-62646434d761)


----------------

# SignLanguageDetector-WithMediapipe

The application was developed using Mediapipe and opencv.
# Hand Gesture Recognition System

This project is a hand gesture recognition system that identifies sign language characters using a computer camera and displays them on the screen. The system was developed using Python and OpenCV and determines sign language characters according to the positions of the hand and the position of the fingers.

## Project Structure

The project consists of two Python files:

- **Function.py**: File where functions and hand gesture recognition algorithms are defined.
- **Main.py**: Main file is used to define hand gestures and visually display them to the user.

### 1. Function.py

Various functions are defined in the Function.py file to determine sign language characters according to the positions of the hand and the position of the fingers.

#### Featured Functions:

- **persons_input(hand_cordinates)**: Gets the coordinates of the hand and identifies the sign language character by determining whether the fingers are up or down.

- **get_fram(image, hand_cordinate, string)**: Draws a red rectangle on the image according to the given coordinates and adds the sign language character.

Below you can see an example usage of one of these functions:

python
def persons_input(hand_cordinates):
def distance(x1, y1, x2, y2):
# Sets the distance with the Euclidean distance formula
distance = int((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2))
return distance

# Logic for determining sign language characters...

return persons_input

### Main.py

The Main.py file is the main runtime file for the project and performs the processes of recognizing sign language characters and displaying them on the screen.

In this file:

- Real-time hand detection is performed using **Mediapipe**.
- Sign language characters are determined using the coordinates of the detected hand.
- Defined characters and hand position are drawn on the screen.
- ### Example Usage

python
import numpy as np
import mediapipe as mp
from Function import *

# Start camera and detect hands
cap = cv.VideoCapture(0)

with mp.solutions.hands.Hands(max_num_hands=1) as hands:
while cap.isOpened():
success, image = cap.read()
if not success:
print("Ignoring empty camera frame.")
continue

# Operation and detection codes...

cv.imshow('Sign Language Detection', cv.flip(image, 1))

# Press 'x' to exit the loop
if cv.waitKey(5) & 0xFF == ord('x'):
break

cap.release()

### Requirements

Libraries required to run the project:

- OpenCV
- Mediapipe
- Numpy

### Installation

To install the necessary libraries, enter the following commands in the terminal:

bash
pip install opencv-python mediapipe numpy

### Usage
Run the Main.py file to start the system. The camera will open and recognize your hand movements and display sign language characters on the screen. Press the 'x' key to exit the program.




