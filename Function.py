import cv2 as cv

def persons_input(hand_cordinates):
    def distance(x1,y1,x2,y2):
        #MESAFEYI AYARLIYORUZ.OKLİD MESAFE FORMULÜ
        distance=int((((x1-x2)**2)+((y1-y2)**2))**(1/2))
        return distance
    
    persons_input=""    #İŞARET DİLİ KARAKTERİNİ SAKLAYACAĞIMIZ İNPUT
    hand_horz=False     #EL YATAYMI DİKEYMİ
    
    thumbs_up=False     #->başparmak   
    index_up=False      #->işaretparmağı
    middel_up=False     #->ortaparmak
    ring_up=False       #->Yüzükparmak
    littel_up=False     #->serçeparmak
    
            

    #başparmak ve orta parmak arasındaki mesafeye bağlı olarak yatay veya dikey olduğunu belirle.
    if distance(hand_cordinates[0][2],0,hand_cordinates[12][2],0) < distance(hand_cordinates[0][1],0,hand_cordinates[12][1],0):
        hand_horz=True


    #Başparmağın yukarıda veya aşşağıda olduğunu belirle
    #                           elin tabanı ile başparmağın ilk eklemi arasındaki mesafe                                    elin tabanı ile başparmağın uç noktası arasındaki mesafe                 
    if distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[3][1],hand_cordinates[3][2]) < distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[4][1],hand_cordinates[4][2]):
        thumbs_up=True  
    if distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[6][1],hand_cordinates[6][2]) < distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[8][1],hand_cordinates[8][2]):
        index_up=True
    if distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[10][1],hand_cordinates[10][2]) < distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[12][1],hand_cordinates[12][2]):
        middel_up=True
    if distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[14][1],hand_cordinates[14][2]) < distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[16][1],hand_cordinates[16][2]):
        ring_up=True
    if distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[18][1],hand_cordinates[18][2]) < distance(hand_cordinates[0][1],hand_cordinates[0][2],hand_cordinates[20][1],hand_cordinates[20][2]):
        littel_up=True
        
    


    #Burada işaret dili karakterlerini belirliyoruz.
    #Herbir karakter için elin ve parmakların pozisyonlarını belirliyoruz.
    #Bu koşullarda başparmak yukarıda * thumbs_up=TRUE ve el yatay değilse:

    if index_up==False and middel_up==False and ring_up==False and littel_up==False and thumbs_up==True and hand_horz==False:
        if distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[16][1],hand_cordinates[16][2]) < distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[13][1],hand_cordinates[13][2]):
            persons_input=" O"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[18][1],hand_cordinates[18][2]) < distance(hand_cordinates[14][1],hand_cordinates[14][2],hand_cordinates[18][1],hand_cordinates[18][2]):
            persons_input=" M"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[18][1],hand_cordinates[18][2]) < distance(hand_cordinates[10][1],hand_cordinates[10][2],hand_cordinates[18][1],hand_cordinates[18][2]):
            persons_input=" N"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[18][1],hand_cordinates[18][2]) < distance(hand_cordinates[6][1],hand_cordinates[6][2],hand_cordinates[18][1],hand_cordinates[18][2]):
            persons_input=" T"
        else :
            persons_input=" A"
    #Tüm parmaklar yukarıda ve el yatay değilse * Hepsi true :         
    elif index_up==True and middel_up==True and ring_up==True and littel_up==True and thumbs_up==True and hand_horz==False:
        if distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[12][1],hand_cordinates[12][2]) < distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[11][1],hand_cordinates[11][2]):
            persons_input=" C"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[17][1],hand_cordinates[17][2]) < distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[5][1],hand_cordinates[5][2]):
            persons_input=" B"
    #Tüm parmaklar aşşağıda ise * Hepsi false :        
    elif index_up==False and middel_up==False and ring_up==False and littel_up==False and thumbs_up==False and hand_horz==False:
        if distance(hand_cordinates[20][1],hand_cordinates[20][2],hand_cordinates[4][1],hand_cordinates[4][2]) < distance(hand_cordinates[19][1],hand_cordinates[19][2],hand_cordinates[4][1],hand_cordinates[4][2]):
            persons_input=" E"
        else:
            persons_input=" S"
    #Orta, yüzük ve serçe parmak yukarıda, baş parmak ve işaret parmak aşağıda ve el yatay değilse:        
    elif index_up==False and middel_up==True and ring_up==True and littel_up==True and thumbs_up==True and hand_horz==False:
        persons_input=" F"
    #İşaret parmak ve baş parmak yukarıda, diğer parmaklar aşağıda ve el yatay ise:    
    elif index_up==True and middel_up==False and ring_up==False and littel_up==False and thumbs_up==True and hand_horz==True:
        if distance(hand_cordinates[8][1],hand_cordinates[8][2],hand_cordinates[4][1],hand_cordinates[4][2]) < distance(hand_cordinates[6][1],hand_cordinates[6][2],hand_cordinates[4][1],hand_cordinates[4][2]):
            persons_input=" Q"
        elif distance(hand_cordinates[12][1],hand_cordinates[12][2],hand_cordinates[4][1],hand_cordinates[4][2]) < distance(hand_cordinates[10][1],hand_cordinates[10][2],hand_cordinates[4][1],hand_cordinates[4][2]):
            persons_input=" P"
        else:
            persons_input=" G"
     ## İşaret parmak ve baş parmak yukarıda, diğer parmaklar aşağıda ve el yatay değilse:       
    elif index_up==True and middel_up==True and ring_up==False and littel_up==False and thumbs_up==True and hand_horz==True:
        if distance(hand_cordinates[12][1],hand_cordinates[12][2],hand_cordinates[4][1],hand_cordinates[4][2]) < distance(hand_cordinates[10][1],hand_cordinates[10][2],hand_cordinates[4][1],hand_cordinates[4][2]):
            persons_input=" P"
        else:
            persons_input=" H"
     ## Serçe parmak yukarıda, diğer parmaklar aşağıda ve el yatay değilse:
    elif index_up==False and middel_up==False and ring_up==False and littel_up==True and thumbs_up==False and hand_horz==False:
        persons_input=" I"
     ## Serçe parmak yukarıda, diğer parmaklar aşağıda ve el yatay ise:   
    elif index_up==False and middel_up==False and ring_up==False and littel_up==True and thumbs_up==False and hand_horz==True:
        persons_input=" J"
     ## İşaret parmak ve baş parmak yukarıda, diğer parmaklar aşağıda ve el yatay değilse:   
    elif index_up==True and middel_up==True and ring_up==False and littel_up==False and thumbs_up==True and hand_horz==False:
        if hand_cordinates[8][1] < hand_cordinates[12][1]:
            persons_input=" R"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[14][1],hand_cordinates[14][2]) < distance(hand_cordinates[9][1],hand_cordinates[9][2],hand_cordinates[14][1],hand_cordinates[14][2]):
            if 2*distance(hand_cordinates[5][1],hand_cordinates[5][2],hand_cordinates[9][1],hand_cordinates[9][2]) < distance(hand_cordinates[8][1],hand_cordinates[8][2],hand_cordinates[12][1],hand_cordinates[12][2]):
                persons_input=" V"
            else:
                persons_input=" U"
        elif distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[14][1],hand_cordinates[14][2]) < distance(hand_cordinates[5][1],hand_cordinates[5][2],hand_cordinates[14][1],hand_cordinates[14][2]):
            persons_input=" K"
     ## İşaret parmak ve baş parmak yukarıda, diğer parmaklar aşağıda ve el yatay değilse:       
    elif index_up==True and middel_up==False and ring_up==False and littel_up==False and thumbs_up==True and hand_horz==False:
        if distance(hand_cordinates[3][1],hand_cordinates[3][2],hand_cordinates[14][1],hand_cordinates[14][2]) < distance(hand_cordinates[14][1],hand_cordinates[14][2],hand_cordinates[4][1],hand_cordinates[4][2]):
            persons_input=" L"
        elif distance(hand_cordinates[8][1],hand_cordinates[8][2],hand_cordinates[10][1],hand_cordinates[10][2]) < distance(hand_cordinates[6][1],hand_cordinates[6][2],hand_cordinates[10][1],hand_cordinates[10][2]):
            persons_input=" X"
        else:
            persons_input=" D"
     ## İşaret ve orta parmaklar yukarıda, yüzük ve serçe parmaklar aşağıda ve baş parmak yatay değilse:       
    elif index_up==True and middel_up==True and ring_up==False and littel_up==False and thumbs_up==False and hand_horz==False:
        if hand_cordinates[8][1] < hand_cordinates[12][1]:
            persons_input=" R"
        elif 2*distance(hand_cordinates[5][1],hand_cordinates[5][2],hand_cordinates[9][1],hand_cordinates[9][2]) < distance(hand_cordinates[8][1],hand_cordinates[8][2],hand_cordinates[12][1],hand_cordinates[12][2]):
            persons_input=" V"
        else:
            persons_input=" U"
     ## İşaret, orta ve yüzük parmakları yukarıda, serçe parmak aşağıda ve baş parmak yatay değilse:       
    elif index_up==True and middel_up==True and ring_up==True and littel_up==False and thumbs_up==True and hand_horz==False:
        persons_input=" W"
     ## Serçe parmak ve baş parmak yukarıda, diğer parmaklar aşağıda ve el yatay değilse:   
    elif index_up==False and middel_up==False and ring_up==False and littel_up==True and thumbs_up==True and hand_horz==False:
        if distance(hand_cordinates[3][1],hand_cordinates[3][2],hand_cordinates[18][1],hand_cordinates[18][2]) < distance(hand_cordinates[4][1],hand_cordinates[4][2],hand_cordinates[18][1],hand_cordinates[18][2]):
            persons_input=" Y"
        else:
            persons_input=" I"
        
    return persons_input

"""
Bu fonksiyon, elin pozisyonlarına ve parmakların durumuna göre belirli işaret dili karakterlerini tanımlar. 
Her durumda, parmakların yukarıda veya aşağıda olması, elin yatay veya dikey olması gibi kriterler kullanılarak hangi işaret dili karakterinin yapıldığı tespit edilir.
Sonuçta elin koordinatlarını analiz ederek doğru karakteri döndürür.

"""

# Görüntüye işaret dili karakterini ekleyen fonksiyon.
def get_fram(image,hand_cordinate,string):
   # Elin en sağ noktasını bulan iç fonksiyon.
   def x_max(hand_cordinate):
      max_val=0
      for cordinate_list in hand_cordinate:
         if max_val<cordinate_list[1]:   
            max_val=cordinate_list[1]
      return max_val
   # Elin en üst noktasını bulan iç fonksiyon.
   def y_max(hand_cordinate):
      max_val=0
      for cordinate_list in hand_cordinate:
         if max_val<cordinate_list[2]:  
            max_val=cordinate_list[2]
      return max_val
   # Elin en sol noktasını bulan iç fonksiyon.
   def x_min(hand_cordinate):
      min_val=hand_cordinate[0][1]
      for cordinate_list in hand_cordinate:
         if min_val>cordinate_list[1]:
            min_val=cordinate_list[1]
      return min_val
   # Elin en alt noktasını bulan iç fonksiyon.
   def y_min(hand_cordinate):
      min_val=hand_cordinate[0][2]
      for cordinate_list in hand_cordinate:
         if min_val>cordinate_list[2]:
            min_val=cordinate_list[2]
      return min_val
   

   # KIRMIZI BIR DIKDORTGEN CIZIP ISARET DILINI OPENCV ILE YAZMA.
   def show_holy_rect(image,start_point,end_point,string):
      maxX=image.shape[1]
      image = cv.rectangle(image, start_point, end_point, (0,0,255), 1)#    koordinatları arasında kırmızı renkte (BGR formatında (0, 0, 255)) ve kalınlığı 1 piksel olan bir dikdörtgen çizer.
      image = cv.rectangle(image,(start_point[0],start_point[1]+23),(end_point[0],start_point[1]+3),(0,0,255),-1)# 2 adet dikdortgen çizip en alttaki dıkdortgende HARFLERI yazıyoruz.
      
      image = cv.putText(cv.flip(image,1),string, (maxX-end_point[0],start_point[1]+20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
      return cv.flip(image,1)#Bu değer, görüntünün hangi eksende yansıtılacağını belirler

   image=show_holy_rect(image,(x_min(hand_cordinate)-7,y_max(hand_cordinate)+7),(x_max(hand_cordinate)+7,y_min(hand_cordinate)-7),string)

   return image
"""
Bu fonksiyon, elin koordinatlarını kullanarak görüntüde elin etrafına kırmızı bir dikdörtgen çizer ve işaret dili karakterini bu dikdörtgenin üstüne ekler. 
Bu da işaret dili karakterlerinin görselleştirilmesini sağlar. 
Etrafında kırmızı bir dikdörtgen olan ve işaret dili karakterini içeren bir görüntü döndürür. """