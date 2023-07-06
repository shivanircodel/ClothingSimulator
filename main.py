SYMBOLS = ['@','#','$','%','=']
top = (1, 2, 3, 4, 5, 6)
top = ["shirt", "sweater", "tank", "TShirt", "dress", "sweatshirt"]
print(top)
bottom = (11, 12, 13, 14, 15)
bottom = ["jeans", "shorts", "pants", "skirt", "sweatpants"]
print(bottom)
def displayListAndNumber(theList):
  def my_color(black, white, pink, yellow, green, red, blue, purple, gray):
    outfit = 0
    print("You should wear" + color)
first_color = ["black", "pink", "green", "blue", "gray", "white"]
print(len(first_color))
second_color = ["black", "yellow", "red", "purple", "white", "gray"]
print(len(second_color))
print ("Welcome to your online clothing simulator!")
name = input ("Please Enter your name:")
print("Nice to meet you ", name)
color = input("Enter your favorite color today:")
top = input("Enter a number from 1-6: ")
help_dict = {
  '1': 'shirt',
  '2': 'tank',
  '3': 'sweater',
  '4': 'sweatshirt',
  '5': 'dress',
  '6': 'TShirt'
}
test_str = top
print("The original string is: " + test_str)
res1 = ''.join(help_dict[ele] for ele in test_str.split())
x = print("The string after performing replace: " + res1)
top == 'x'
for x in top:
  print(x)
if x == 1:
  print('shirt')
else:
  if x == 2:
    print('tank')
  else:
    if x == 3:
      print('sweater')
    else:
      if x == 4:
        print('sweatshirt')
      else:
        if x == 5:
          print('dress')
        else:
          if x == 6:
            print('TShirt')
print('top is:', res1)
bottom = input("Enter a number from 11-15: ")
help_dict = {
  '11': 'jeans',
  '12': 'shorts',
  '13': 'pants',
  '14': 'skirt',
  '15': 'sweatpants'
}
test_str = bottom
print("the original string is: " + test_str)
res = ''.join(help_dict[ele] for ele in test_str.split())
y = print("The string after performing replace: " + res)
for y in bottom:
  print(y)
if y == 11:
  print('jeans')
else:
  if y == 12:
    print('shorts')
  else:
    if y == 13:
      print('pants')
    else: 
      if y == 14:
        print('skirt')
      else:
        if y == 15:
          print('sweatpants')
print('bottom is:', res)
color2 = input("What is your second favorite color today?")
shoe = input("What did you eat for breakfast yesterday?: ")
if (shoe == "oatmeal"):
  shoe = print("You will be wearing sneakers today")
else:
  shoe = input("fruits or veggies?: ")
  if (shoe == "fruits"):
   shoe = print("You will be wearing boots today")
  else: 
    shoe = print("You will be wearing flipflops/sandals today")
  print("Let's choose a headware for you")
headOther = input("Choose a special character: ")
help_dict = {
  '@': 'hat',
  '#': 'headband',
  '$': 'cap',
  '%': 'hairclip'
}
test_str = headOther
print("the original string is: " + test_str)
headOther = ''.join(help_dict[ele] for ele in test_str.split())
print("The string after performing replace: " + headOther)
if 'headOther' == '@':
  print("You will be wearing a hat along with your outfit today")
else:
  if 'headOther' == '#':
    print("You will be wearing a headband today")
  else:
    if 'headOther' == '$':
      print("You will be wearing a cap today")
    else:
      if 'headOther' == '%':
        print("You will be wearing a hair clip today")
      else:
        if 'headOther' == '&':
          print("You will not be wearing anything on your head today")
print("head is", headOther)
print("Let's choose an accessory for you")
accOther = input("Choose a letter from B-F: ")
help_dict = {
  'B': 'scarf',
  'C': 'Necklace',
  'D': 'bracelet/watch',
  'E': 'ring',
  'F': 'nothing'
}
test_str = accOther
accOther = ''.join(help_dict[ele] for ele in test_str.split())
print("The string after performing replace: " + accOther)
if 'accOther' == 'B':
  print("You will be wearing a scarf today")
else:
  if 'accOther' == 'C':
    print("You will be wearing a necklace today")
  else:
    if 'accOther' == 'D':
      print("You will be wearing a bracelet/watch today")
    else:
      if 'accOther' == 'E':
        print("You will be wearing a ring ")
      else:
        if 'accOther' == 'F':
          print("You will not be wearing any accessories today")
print("accessory is", accOther)
print("Today you will be wearing a ", color, "colored", res1, " a", color2, "colored",res , "along with a ", headOther,"a", accOther,"and a", shoe)     
