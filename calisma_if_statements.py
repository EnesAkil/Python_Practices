# -*- coding: utf-8 -*-
"""calisma_if_statements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K2xY6ZvJo2qcQ2sZysa8UvlPtEvQW2_Y
"""

if True:
  print('It is true')

empty_seat = 25
if empty_seat > 10 :
    print('There is still seat to sit')

# == equality
# != not equal
# > graeter than another value
# < less than
# >= greater than or equal
# <= less than or equal

# if condition1:
    # execute body1
# else :
    # execute body2

course = input('which course do you prefer :')
if course == 'clarusway':
  print('you guarenteed the job')
else :
  print('think about again')

basket = ['apple','peach','blackberry']
fruit = 'cherry'
if fruit not in basket:
  print('I can have a little')
else:
  print('I have already')

"""elif*********

"""

weight = int(input('please write your weight : '))
if weight > 100 :
  print('You are fat')
elif weight >= 75 :
  print('You are fit')
else :
  print('You are thin')

number = 8
if number >= 10:
  print('The number is equal or greater than 10')
else:
  print('The number is less than 10')

siparis = (input('Hoş geldiniz ne arzu edersiniz :'))
menu = 'çipura','adana kebap','imam bayildi','baklava'

if siparis in menu:
    if siparis == 'çipura':
      print('Harika bir tercih yaptınız balıklarımız günlük ve taze gelmektedir')
    elif siparis == 'adana kebap':
      print('Ağzınızın tadini biliyorsunuz. Kebap ustamız has Adanalıdır.')
    elif siparis == 'imam bayildi':
      print('Bu lezzete sadece imam değil yiyen herkes bayılıyor.')
    else:
      print("Gaziantep'in en güzel baklavalarından birini seçtiniz.")
else:
  print('Maalesef taze bitti.')

