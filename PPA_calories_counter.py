#author: Pavel Ponomarev
import csv

kcal_dict = {
  'Apple' : 45,
  'Apricot' : 17,
  'Banana' : 80,
  'Blackberries' : 28,
  'Blueberries' : 51,
  'Cherries' : 40,
  'Clementine' : 20,
  'Cranberries' : 46,
  'Gooseberries' : 46,
  'Grapefruit' : 20,
  'Grapes' : 60,
  'Kiwi' : 25,
  'Lemon' : 14,
  'Lime' : 11,
  'Mandarin' : 20,
  'Mango' : 95,
  'Melon' : 21,
  'Nectarine' : 50,
  'Orange' : 48,
  'Peach' : 36,
  'Pear' : 48,
  'Pineapple' : 42,
  'Plum' : 20,
  'Pomegranate' : 100,
  'Rasberries' : 24,
  'Rhubarb' : 21,
  'Satsuma' : 20,
  'Strawberries' : 24,
  'Tangerine' : 20,
  }

other_list = [
  'Blackberries',
  'Blueberries', 
  'Cherries',
  'Cranberries',
  'Grapes',
  'Rasberries',
  'Strawberries',
  'Melon',
  'Pinaple'
  ]

fruit_name = None
fruit_counter = None
kcal_counter = None
all_calories = 0
list_check = []

while True:
  print('Please, enter current date :', '\n(example: 25/10/20)')
  current_date = str(input())
  if int(current_date[0]+current_date[1])>31:
    print('Incorrect date (days)')
  elif int(current_date[3]+current_date[3])>12:
      print('Incorrect date (months)')
  elif current_date[2] != '/':
    print('Incorrect date (format)')
  elif current_date[5] != '/':
    print('Incorrect date (format)')
  else:
    break

print('Did you eat any fruits today? \nY/N?')
while True:
  fruit_eating_question = str(input())
  if fruit_eating_question == 'N':
    print('No fruits today? \nMaybe have some? ')
  else:
    break

with open('calories.csv', mode = 'w') as calories:
  data_writer = csv.writer(calories, delimiter = ',')
  data_writer.writerow(['Date', 'Fruit', 'Quantity', 'Fruit calories', 'Total calories'])
  while True:
    if fruit_eating_question == 'Y' or 'Yes':
      print('Please, enter fruit name bellow:\n(example: Apple)')
    fruit_name = str(input())
    for key in kcal_dict:
      list_check.append(key)
    if fruit_name not in list_check:
      print('There is no such fruit in the list or you have a mistake while writing!','\n Try one more time!')
      fruit_name = str(input())
    for key in kcal_dict:
      if fruit_name == key:
        if fruit_name in other_list:
          print('How many grams of', fruit_name,' did you eat today?')
          fruit_counter = int(input())
          kcal_counter = fruit_counter * kcal_dict[key] / 100
          all_calories += kcal_counter
          data_writer.writerow([current_date, key, fruit_counter, kcal_counter, all_calories])
        elif fruit_name == 'Grapefruit':
          fruit_name += 's'
          print('How many ', fruit_name,' did you eat today?')
          fruit_counter = int(input())
          kcal_counter = fruit_counter * kcal_dict[key] * 2
          all_calories += kcal_counter
          data_writer.writerow([current_date, key, fruit_counter, kcal_counter, all_calories])
        else:
          fruit_name += 's'
          print('How many ', fruit_name,' did you eat today?')
          fruit_counter = int(input())
          kcal_counter = fruit_counter * kcal_dict[key]
          all_calories += kcal_counter
          data_writer.writerow([current_date, key, fruit_counter, kcal_counter, all_calories])
    print('Would you like to add another fruit? \nY/N')
    fruit_eating_question = str(input())
    if fruit_eating_question == 'Y':
      continue
    else:
      print('Ok, your total calories consumption is:', all_calories)
      data_writer.writerow(['Total calories for', current_date, 'is', all_calories])
      break
