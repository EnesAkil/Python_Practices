# -*- coding: utf-8 -*-
"""calisma_loop_while_for.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DpBcGJbHy-aOIajo-sBvOwlQNdeugwZ9
"""

# two major loop statements are while and for

"""While loop*****"""

number = int(input('lütfen 1 ile 9 arasında bir rakam girin :'))
while number < 9:
      print(number)
      number == number
print('girdiğiniz sayi aralik disinda')

i = 0
while (i<=100):
    print(i)
    i += 10

x = 0
while x < 99:            # while ile 3'e bölünebilen sayılar
  print(x)
  x += 3
print("3'e bölünebilen 2 basamaklı en büyük sayi : " ,x)

gün_sayisi = 1
tavan = 440
while gün_sayisi < 10:
  print(gün_sayisi,tavan)
  gün_sayisi += 1
  tavan *= 1.1

i = 1
while True:
  print(i)
  i += 1
  if i == 10000:
    break

i = 1
while True:
  if i % 2 == 0 :
    i += 1
    continue
    print(i)
    if i == 1000:
      break

"""For loop *******

"""

liste = [1,2,3,4,5,6]
for rakam in liste: 
  print(rakam)

isim_listesi = ['ahmet','enes','betül','gökçe']
for isim in isim_listesi:
  print(isim)

for i in range(0,11,2):
    print(i)

sonuc = 1
for i in range (0,10):
  sonuc *= 2
print(sonuc)

tavan = 440
for i in range (0,6):
  tavan *= 1.1
  print(f"{tavan:.2f}")

tavan = 440
for i in range (0,6):
  tavan *= 1.1
print(f"{tavan:.2f}")

liste1 = ["a","b","c"]
liste2 = [1,2,3]
for harf in liste1:
    for rakam in liste2:
      print(harf,rakam)

liste

for i in liste:
  if i == 3:
    print("bu karakter atlanmıştır")
    continue
  print(i)

for i in liste:
  if i == 3:
    print("liste burada sona erdi")
    break
  print(i)

bolme_list = range(101)

for i in bolme_list:                  # 3'e bölünebilen sayıları yazdırma
  if i %3 != 0:
    continue
  print(i)

"""**Examples**"""

cevap = 5103

soru = "Apolet numaramı tahmin edebilir misin?"
print("Hadi tahmin oyunu oynayalım.")

while True:
  tahmin = int(input(soru))

  if tahmin < cevap:
    print("Biraz yukarı")
  elif tahmin > cevap:
    print("Biraz aşağı")
  else:
    print("Harika cevabı buldun. Nereden biliyorsun, sen kahin misin?!!")
    break

iterable = [1,2,3,4]
for i in iterable:
  i *= i
  print(i)

print(*range(5))

a = 3
while a**2 < 299:
  print('I will stop smoking')
  a += 3

total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")
    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")

ps4_price = 500
saved_amount = int(input('Please enter your saved amount: '))

while True:
  if saved_amount >= ps4_price:
    print('Yippee! You can buy your PS4')
  elif saved_amount < (ps4_price)/2:
    print("You must save more, keep saving!")
  elif saved_amount > (ps4_price)/2:
    print("You saved more than half, keep saving!")
  break

math_mark = int(input('Please enter the mark: '))
while True:
  if math_mark >= 85:
    print('A (Excellent)')
  elif math_mark >= 70:
    print('B (Good)')
  elif math_mark >= 60:
    print('C (Medium)')
  elif math_mark >= 45:
    print('D (Not Bad)')
  elif math_mark <= 44:
    print('F (Failed)')
  break

a = int(input('Please enter a number :'))

if a >= 999 :
    print(a ** 0)  

else :
    print(a * 2)

a = 5
b = 3
print(max)

a = 49
while a <= 62:
  print (a)
  a +=5

a = 49
while a % 2 != 0:
  print (a)
  a +=5

a = 49
while a > 10:
  print (a)
  a +=5

month = "August"
spring = "September, April, January"
autumn = "March, October, July"

if (month in spring) or (month in autumn):
    if month in autumn:
        print("This is a spring month")
    else:
        print("This is an autumn month")
else:
    print("This month is not categorized")

number = int(input("Enter a number: "))
i = 0
while i < number:
    print(i**2)
    i += 1

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for item in sample_list:
    print("The type of", item, "is", type(item))

sum_num = 0
for i in range (1,75):
  sum_num += i
print(sum_num)

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

prime=[]  # created an empty list to collect prime numbers in it

for num in range(2, 101):
    status = True
    for i in range(2, num):
        if num % i == 0: # check if the only factors are 1 and itself
            status = False
    if status:
        prime.append(num)  # collect prime numbers in the list

print(prime)                                                                                  # 100' kadar olan asal sayılar

