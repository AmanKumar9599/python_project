#Password Generator Project
import random
letters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
lr_letters = int(input("How many lower case letters would you like in your password?\n")) 
ur_letters = int(input("How many upper case letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
if (lr_letters+nr_numbers+nr_symbols+ur_letters) <=8 and (ur_letters+lr_letters+nr_numbers+nr_symbols)>=16:
  print('Your password should contain 8 to 16 digits')
else:
  password1=""
  for char in range(1, lr_letters + 1):
    password1 += random.choice(letters1)

  for char in range(1, ur_letters + 1):
    password1 += random.choice(letters2)

  for char in range(1, nr_symbols + 1):
    password1 += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password1 += random.choice(numbers)
  password_list =list(password1)
  random.shuffle(password_list)
  st=''
  st=st.join(password_list)
  print(st)
