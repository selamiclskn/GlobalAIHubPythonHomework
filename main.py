

#SOKAĞA ÇIKMA YASAĞI SORGULAMA PROGRAMI


print("Covid-19 tedbirleri sebebiyle getirilen sokağa çıkma yasağı sorgulama ekranına hoşgeldiniz...\n"
      "sorgulama yapmak için aşağıdaki bilgileri dolrunuz.")
ad=input("adınızı giriniz: ")
soyad=input("soyadınızı giriniz: ")
yas=int(input("yaşınızı giriniz: "))
dogum_yili=int(input("doğum yilinizi giriniz: "))
bilgiler=[ad,soyad,yas,dogum_yili]
for i in bilgiler:
    print(i)
if yas>=18:
    print("Sokağa çıkma yasağı kapsamında değilsiniz. Maskemizi takalım ve sosyal mesafeye dikkat edelim.")
elif yas<18:
    print("Sokağa çıkma yasağı kapsamındasınız. #hayatevesıgar  ")