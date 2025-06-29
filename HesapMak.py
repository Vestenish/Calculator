
while True:
   
   
 try: 
    giriş_mesaji = input("Hangi işlemi yapmak istersiniz ? ")  
    soru = eval(giriş_mesaji)   # Kullanıcıya sorulan soru ve soru değişkeninin değişerek 
    print(soru)                 # Verdiği cevap
    if isinstance(soru , (float,int)):
      print("İşlem başarılı.")  
      break        
    else:
       print("İşlem başarısız.")
 except(ValueError , TypeError, ZeroDivisionError, SyntaxError):
      print("Lütfen bir matematiksel işlem giriniz.")





